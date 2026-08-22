from fastapi import APIRouter, HTTPException
from database import supabase
from schemas import LeaveRequestCreate, LeaveApproval

router = APIRouter(
    prefix="/leave",
    tags=["Leave Management"]
)


# Employee applies for leave
@router.post("/apply")
def apply_for_leave(request: LeaveRequestCreate):

    # Check employee exists
    employee = (
        supabase
        .table("users")
        .select("id")
        .eq("id", request.employee_id)
        .execute()
    )

    if not employee.data:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # Validate date range
    if request.end_date < request.start_date:
        raise HTTPException(
            status_code=400,
            detail="End date cannot be before start date"
        )

    # Validate leave type
    if request.leave_type not in ["Paid", "Sick", "Unpaid"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid leave type"
        )

    leave_request = {
        "employee_id": request.employee_id,
        "leave_type": request.leave_type,
        "start_date": request.start_date.isoformat(),
        "end_date": request.end_date.isoformat(),
        "remarks": request.remarks,
        "status": "Pending"
    }

    response = (
        supabase
        .table("leave_requests")
        .insert(leave_request)
        .execute()
    )

    return {
        "message": "Leave request submitted successfully",
        "leave_request": response.data
    }


# Employee views their leave requests
@router.get("/employee/{employee_id}")
def get_employee_leave(employee_id: int):

    response = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("employee_id", employee_id)
        .execute()
    )

    return {
        "leave_requests": response.data
    }


# Admin/HR views all leave requests
@router.get("/all")
def get_all_leave_requests():

    response = (
        supabase
        .table("leave_requests")
        .select("*")
        .execute()
    )

    return {
        "leave_requests": response.data
    }


# Admin/HR views one leave request
@router.get("/{leave_id}")
def get_leave_request(leave_id: int):

    response = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("id", leave_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Leave request not found"
        )

    return response.data[0]


# Admin/HR approves or rejects leave
@router.put("/{leave_id}/status")
def update_leave_status(
    leave_id: int,
    approval: LeaveApproval
):

    if approval.status not in ["Approved", "Rejected"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Approved or Rejected"
        )

    existing_request = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("id", leave_id)
        .execute()
    )

    if not existing_request.data:
        raise HTTPException(
            status_code=404,
            detail="Leave request not found"
        )

    update_data = {
        "status": approval.status,
        "admin_comment": approval.admin_comment
    }

    response = (
        supabase
        .table("leave_requests")
        .update(update_data)
        .eq("id", leave_id)
        .execute()
    )

    return {
        "message": "Leave request updated successfully",
        "leave_request": response.data
    }
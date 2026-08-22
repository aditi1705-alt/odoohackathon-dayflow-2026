from fastapi import APIRouter, HTTPException
from app.models.attendance import AttendanceCheckIn
from app.services.attendance_service import (
    check_in_employee,
    check_out_employee,
    get_attendance_history
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/check-in")
def check_in(data: AttendanceCheckIn):
    result = check_in_employee(data.employee_id)

    if "error" in result:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result


@router.post("/check-out/{employee_id}")
def check_out(employee_id: str):
    result = check_out_employee(employee_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="No attendance record found for today"
        )

    return result


@router.get("/{employee_id}")
def get_history(employee_id: str):
    return get_attendance_history(employee_id)
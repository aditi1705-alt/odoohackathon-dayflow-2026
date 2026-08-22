from fastapi import APIRouter, HTTPException

from app.services.dashboard_service import (
    get_employee_dashboard,
    get_recent_activity,
    get_all_employees,
    get_employee_for_hr,
    get_pending_leave_requests
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/employee/{employee_id}")
def employee_dashboard(employee_id: int):

    dashboard = get_employee_dashboard(employee_id)

    if dashboard is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return dashboard


@router.get("/employee/{employee_id}/activity")
def employee_activity(employee_id: int):

    activity = get_recent_activity(employee_id)

    return activity


@router.get("/hr/employees")
def hr_employees():

    employees = get_all_employees()

    return {
        "employees": employees
    }


@router.get("/hr/employee/{employee_id}")
def hr_employee(employee_id: int):

    employee = get_employee_for_hr(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.get("/hr/leave-requests")
def hr_leave_requests():

    requests = get_pending_leave_requests()

    return {
        "leave_requests": requests
    }
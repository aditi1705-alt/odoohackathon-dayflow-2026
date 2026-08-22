from fastapi import APIRouter
from app.models.payroll import PayrollCreate
from app.services.payroll_service import (
    create_payroll,
    get_employee_payroll
)

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@router.post("/")
def add_payroll(data: PayrollCreate):
    return create_payroll(
        employee_id=data.employee_id,
        basic_salary=data.basic_salary,
        allowances=data.allowances,
        deductions=data.deductions
    )


@router.get("/{employee_id}")
def get_payroll(employee_id: str):
    return get_employee_payroll(employee_id)
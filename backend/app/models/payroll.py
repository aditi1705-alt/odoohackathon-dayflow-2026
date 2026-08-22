from pydantic import BaseModel


class PayrollCreate(BaseModel):
    employee_id: str
    basic_salary: float
    allowances: float = 0
    deductions: float = 0


class PayrollUpdate(BaseModel):
    basic_salary: float
    allowances: float = 0
    deductions: float = 0
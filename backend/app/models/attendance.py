from pydantic import BaseModel
from typing import Optional


class AttendanceCheckIn(BaseModel):
    employee_id: str


class AttendanceRecord(BaseModel):
    employee_id: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    status: Optional[str] = "Present"
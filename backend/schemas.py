from pydantic import BaseModel
from datetime import date
from typing import Optional


class LeaveRequestCreate(BaseModel):
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    remarks: Optional[str] = None

class UserCreate(BaseModel):
    name:str
    email:str
    role:str="Employee"
    department:Optional[str]=None

class LeaveApproval(BaseModel):
    status:str
    admin_comment:Optional[str]=None
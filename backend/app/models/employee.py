from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: str
    name: str
    designation: str
    role: str  # "admin" or "employee"
    status: str  # "present" | "leave" | "absent"
    avatar_url: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    monthly_wage: Optional[float] = None
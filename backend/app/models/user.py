from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: str
    role: str = "Employee"
    department: Optional[str] = None
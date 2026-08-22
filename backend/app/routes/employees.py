from fastapi import APIRouter, HTTPException
from config.supabase_client import supabase

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/")
def get_employees():
    result = supabase.table("Employees").select("*").execute()
    return result.data

@router.get("/{employee_id}")
def get_employee(employee_id: str):
    result = supabase.table("Employees").select("*").eq("id", employee_id).single().execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result.data
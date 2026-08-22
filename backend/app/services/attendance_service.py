from datetime import datetime
from app.services.supabase import supabase


def check_in_employee(employee_id: str):
    today = datetime.now().date().isoformat()

    existing = (
        supabase.table("attendance")
        .select("*")
        .eq("employee_id", employee_id)
        .eq("attendance_date", today)
        .execute()
    )

    if existing.data:
        return {"error": "Employee has already checked in today"}

    data = {
        "employee_id": employee_id,
        "attendance_date": today,
        "check_in": datetime.now().isoformat(),
        "status": "Present"
    }

    response = supabase.table("attendance").insert(data).execute()

    return response.data[0]


def check_out_employee(employee_id: str):
    today = datetime.now().date().isoformat()

    response = (
        supabase.table("attendance")
        .select("*")
        .eq("employee_id", employee_id)
        .eq("attendance_date", today)
        .execute()
    )

    if not response.data:
        return None

    record = response.data[-1]

    updated = (
        supabase.table("attendance")
        .update({
            "check_out": datetime.now().isoformat()
        })
        .eq("id", record["id"])
        .execute()
    )

    return updated.data[0]


def get_attendance_history(employee_id: str):
    response = (
        supabase.table("attendance")
        .select("*")
        .eq("employee_id", employee_id)
        .order("attendance_date", desc=True)
        .execute()
    )

    return response.data
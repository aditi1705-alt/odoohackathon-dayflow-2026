from app.services.supabase import supabase


def get_employee_dashboard(employee_id: int):
    # Employee profile
    employee_response = (
        supabase
        .table("users")
        .select("*")
        .eq("id", employee_id)
        .execute()
    )

    if not employee_response.data:
        return None

    employee = employee_response.data[0]

    # Attendance
    attendance_response = (
        supabase
        .table("attendance")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("attendance_date", desc=True)
        .limit(10)
        .execute()
    )

    # Leave requests
    leave_response = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("employee_id", employee_id)
        .order("start_date", desc=True)
        .limit(10)
        .execute()
    )

    return {
        "employee": employee,
        "attendance": attendance_response.data,
        "leave_requests": leave_response.data
    }


def get_recent_activity(employee_id: int):
    attendance_response = (
        supabase
        .table("attendance")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("attendance_date", desc=True)
        .limit(5)
        .execute()
    )

    leave_response = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("employee_id", employee_id)
        .order("start_date", desc=True)
        .limit(5)
        .execute()
    )

    return {
        "attendance": attendance_response.data,
        "leave_requests": leave_response.data
    }


def get_all_employees():
    response = (
        supabase
        .table("users")
        .select("*")
        .execute()
    )

    return response.data


def get_employee_for_hr(employee_id: int):
    employee_response = (
        supabase
        .table("users")
        .select("*")
        .eq("id", employee_id)
        .execute()
    )

    if not employee_response.data:
        return None

    employee = employee_response.data[0]

    attendance_response = (
        supabase
        .table("attendance")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("attendance_date", desc=True)
        .execute()
    )

    leave_response = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("employee_id", employee_id)
        .order("start_date", desc=True)
        .execute()
    )

    return {
        "employee": employee,
        "attendance": attendance_response.data,
        "leave_requests": leave_response.data
    }


def get_pending_leave_requests():
    response = (
        supabase
        .table("leave_requests")
        .select("*")
        .eq("status", "Pending")
        .execute()
    )

    return response.data
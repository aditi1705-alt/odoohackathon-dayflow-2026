from app.services.supabase import supabase


def create_payroll(
    employee_id,
    basic_salary,
    allowances,
    deductions
):
    net_salary = basic_salary + allowances - deductions

    data = {
        "employee_id": employee_id,
        "basic_salary": basic_salary,
        "allowances": allowances,
        "deductions": deductions,
        "net_salary": net_salary
    }

    response = supabase.table("payroll").insert(data).execute()

    return response.data[0]


def get_employee_payroll(employee_id):
    response = supabase.table("payroll") \
        .select("*") \
        .eq("employee_id", employee_id) \
        .order("created_at", desc=True) \
        .execute()

    return response.data
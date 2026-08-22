from fastapi import APIRouter, HTTPException
from app.services.supabase import supabase
from app.models.user import UserCreate


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users():

    response = (
        supabase
        .table("users")
        .select("*")
        .execute()
    )

    return {
        "users": response.data
    }


@router.get("/{user_id}")
def get_user(user_id: int):

    response = (
        supabase
        .table("users")
        .select("*")
        .eq("id", user_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return response.data[0]


@router.post("/")
def create_user(user: UserCreate):

    new_user = {
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "department": user.department
    }

    response = (
        supabase
        .table("users")
        .insert(new_user)
        .execute()
    )

    return {
        "message": "User created successfully",
        "user": response.data
    }
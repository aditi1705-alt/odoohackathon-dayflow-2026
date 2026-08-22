from fastapi import FastAPI

from routes.users import router as users_router
from routes.leave import router as leave_router


app = FastAPI(
    title="Leave & Time-Off Management API"
)


app.include_router(users_router)
app.include_router(leave_router)


@app.get("/")
def home():

    return {
        "message": "Leave Management API is running"
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes import attendance, payroll,leave,users


app = FastAPI(title="DayFlow API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(attendance.router)
app.include_router(payroll.router)
app.include_router(leave.router)
app.include_router(users.router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import attendance, payroll, employees

app = FastAPI(
    title="DayFlow API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only — restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(attendance.router)
app.include_router(payroll.router)
app.include_router(employees.router)

@app.get("/")
def root():
    return {
        "message": "DayFlow API is running"
    }
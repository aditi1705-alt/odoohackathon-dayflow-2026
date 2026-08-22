from fastapi import FastAPI
from app.routes import attendance, payroll

app = FastAPI(
    title="DayFlow API"
)

app.include_router(attendance.router)
app.include_router(payroll.router)


@app.get("/")
def root():
    return {
        "message": "DayFlow API is running"
    }
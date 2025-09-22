# app/main.py
from fastapi import FastAPI
from app.routes import student, admin, common

app = FastAPI(title="Campus Backend API")

# include routers
app.include_router(student.router)
app.include_router(admin.router)
app.include_router(common.router)

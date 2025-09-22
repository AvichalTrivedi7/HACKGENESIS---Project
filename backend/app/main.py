from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routes import student, admin, common


app = FastAPI(title="Campus Backend API")


# Allow CORS from local frontend for demo purposes
app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


app.include_router(student)
app.include_router(admin)
app.include_router(common)


@app.get("/")
def root():
    return {"message": "HACKGENESIS Backend - alive"}
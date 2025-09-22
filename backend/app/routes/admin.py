from fastapi import APIRouter
from app.mockdata import students, admins   


router = APIRouter(prefix="/admin", tags=["Admin APIs"])


@router.get("/all_students")
def get_all_students():
    return {"students": list(students.keys())}



@router.post("/announcement")
def make_announcement(message: str):
    for s in students.values():
        s["notifications"].append(message)
    return {"status": "Announcement added for all students"}
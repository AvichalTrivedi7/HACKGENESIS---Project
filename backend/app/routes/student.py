from fastapi import APIRouter, HTTPException
from app.mockdata import students


router = APIRouter(prefix="/student", tags=["Student APIs"])


@router.get("/{student_id}/profile")
def get_profile(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    s = students[student_id]
    return {"id": student_id, "name": s["name"], "role": s["role"]}


@router.get("/{student_id}/library")
def get_library(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"due_books": students[student_id]["library"]}


@router.get("/{student_id}/exams")
def get_exams(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"exam_dates": students[student_id]["exams"]}


@router.get("/{student_id}/courses")
def get_courses(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"courses": students[student_id]["courses"]}


@router.get("/{student_id}/grades")
def get_grades(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"grades": students[student_id]["grades"]}


@router.get("/{student_id}/notifications")
def get_notifications(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"notifications": students[student_id]["notifications"]}
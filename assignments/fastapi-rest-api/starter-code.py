from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Homework Tracker API")


class AssignmentCreate(BaseModel):
    title: str
    course: str
    due_date: date


assignments = [
    {
        "id": 1,
        "title": "Finish Python worksheet",
        "course": "Computer Science",
        "due_date": date(2026, 3, 18),
        "completed": False,
    }
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Homework Tracker API"}


@app.get("/assignments")
def list_assignments():
    return assignments


@app.post("/assignments")
def create_assignment(item: AssignmentCreate):
    new_assignment = {
        "id": len(assignments) + 1,
        "title": item.title,
        "course": item.course,
        "due_date": item.due_date,
        "completed": False,
    }
    assignments.append(new_assignment)
    return new_assignment


@app.get("/assignments/{assignment_id}")
def get_assignment(assignment_id: int):
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            return assignment
    raise HTTPException(status_code=404, detail="Assignment not found")


@app.put("/assignments/{assignment_id}/complete")
def complete_assignment(assignment_id: int):
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            assignment["completed"] = True
            return assignment
    raise HTTPException(status_code=404, detail="Assignment not found")


# Run locally with:
# uvicorn starter-code:app --reload
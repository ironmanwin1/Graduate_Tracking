from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/student/{student_id}")
def get_student(student_id: str): 
    with open("mock_data/student.json", "r", encoding="utf-8") as f:
        students = json.load(f)
    for s in students:
        if s["student_id"] == student_id:
            return s
    return {"error": "Student not found"}

@app.get("/form/{student_id}/{form_id}")
def get_student_form(student_id: str, form_id: str):
    filename = f"{student_id}_{form_id}.pdf"
    file_path = f"mock_files/{filename}"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename, media_type="application/pdf")
    return {"error": "File not found"}

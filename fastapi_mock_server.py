from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS: ให้ Flet App เรียกจาก localhost ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# โหลดข้อมูล mock จากไฟล์ student.json
@app.get("/api/student/{student_id}")
def get_student(student_id: str): 
    with open("mock_data/student.json", "r", encoding="utf-8") as f:
        students = json.load(f)
    for s in students:
        if s["student_id"] == student_id:
            return s
    return {"error": "Student not found"}

@app.get("/api/form")
def get_form():
    try:
        with open("mock_data/form.json", "r", encoding="utf-8") as f:
            form_data = json.load(f)
        return form_data
    except Exception as e:
        return {"error": "Unable to load form data", "detail": str(e)}




mock_profiles = [
    {
        "id": "65030226",
        "name_th": "วัชรากร น้อยพันธ์ดี",
        "name_en": "Watcharakorn Noipandee",
        "year": "2565",
        "term": "1",
        "status": "out of condition",
        "semester": "2",
        "edu_year": "2570"
    },
    
]

def get_profile_by_id(student_id: str):
    return next((s for s in mock_profiles if s["id"] == student_id), None)

def load_mock_student_profile():
    import json
    with open("mock_data/student.json", "r", encoding="utf-8") as f:
        return json.load(f)

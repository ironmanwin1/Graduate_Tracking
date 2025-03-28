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
    {
        "id": "65099999",
        "name_th": "สุรศักดิ์ มีใจ",
        "name_en": "Surasak Meejai",
        "year": "2566",
        "term": "2",
        "status": "active",
        "semester": "1",
        "edu_year": "2569"
    }
]

def get_profile_by_id(student_id: str):
    return next((s for s in mock_profiles if s["id"] == student_id), None)
mock_documents = [
    {
        "id": "001",
        "title": "ขอสอบประมวลความรู้",
        "description": "นักศึกษารอการอนุมัติจากอาจารย์",
        "status": "รอดำเนินการ",
        "submit_date": "2024-11-01"
    },
    {
        "id": "002",
        "title": "แบบฟอร์มขอสอบวิทยานิพนธ์",
        "description": "ผ่านการอนุมัติแล้ว",
        "status": "เสร็จสิ้น",
        "submit_date": "2024-09-15"
    }
]

def get_document_by_id(doc_id: str):
    return next((doc for doc in mock_documents if doc["id"] == doc_id), None)

def load_mock_documents():
    import json
    with open("mock_data/documents.json", "r", encoding="utf-8") as f:
        return json.load(f)

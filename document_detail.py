import flet as ft
import httpx

def get_document_from_api(doc_id: str):
    """
    ดึงข้อมูลเอกสารจาก FastAPI mock server
    """
    try:
        url = f"http://127.0.0.1:8000/api/document/{doc_id}"
        res = httpx.get(url)
        if res.status_code == 200:
            doc = res.json()
            # ถ้าเจอ "error" ใน JSON
            if "error" in doc:
                return {
                    "title": "ไม่พบเอกสาร",
                    "status": "-",
                    "description": doc["error"]
                }
            return doc
        else:
            return {
                "title": "ไม่พบเอกสาร",
                "status": "-",
                "description": "ไม่พบรายละเอียดของเอกสารนี้"
            }
    except Exception as e:
        return {
            "title": "Error",
            "status": "-",
            "description": str(e)
        }

def DocumentDetailView(page: ft.Page):
    # ดึง doc_id จาก client_storage (มาจากหน้า Home)
    doc_id = page.client_storage.get("doc_id")

    # เรียกข้อมูลเอกสารจาก API
    doc = get_document_from_api(doc_id)

    # UI เดิม (ไม่เปลี่ยนโครงสร้าง)
    return ft.View(
        route="/document",
        controls=[
            ft.AppBar(
                title=ft.Text("รายละเอียดเอกสาร"),
                bgcolor="#e91e63",
                center_title=True,
                leading=ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    on_click=lambda e: page.go("/home")
                ),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text(doc.get("title", ""), size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        f"สถานะ: {doc.get('status', '')}",
                        size=14,
                        color="green" if doc.get("status", "") == "เสร็จสิ้น" else "orange"
                    ),
                    ft.Divider(height=20),
                    ft.Text(doc.get("description", ""), size=14),
                ], spacing=10),
                padding=20
            )
        ]
    )

import flet as ft

def DocumentDetailView(page: ft.Page):
    # ดึง doc_id จาก client_storage
    doc_id = page.client_storage.get("doc_id")

    # mock ข้อมูลเอกสาร
    mock_documents = {
        "001": {
            "title": "ขอสอบประมวลความรู้ / ใบคำร้องขอสอบปลายภาค",
            "status": "รอดำเนินการ",
            "description": "นักศึกษาต้องยื่นใบคำร้องเพื่อดำเนินการสอบประมวลความรู้"
        },
        "002": {
            "title": "ขอสอบวิทยานิพนธ์ / รับรองหัวข้อวิทยานิพนธ์",
            "status": "เสร็จสิ้น",
            "description": "วิทยานิพนธ์ผ่านการตรวจสอบและรับรองเรียบร้อยแล้ว"
        },
        "003": {
            "title": "ขออนุมัติเค้าโครง / แจ้งชื่อกรรมการสอบเค้าโครง",
            "status": "รอดำเนินการ",
            "description": "อยู่ระหว่างรอการอนุมัติเค้าโครงและแต่งตั้งกรรมการสอบ"
        }
    }

    doc = mock_documents.get(doc_id, {
        "title": "ไม่พบเอกสาร",
        "status": "-",
        "description": "ไม่พบรายละเอียดของเอกสารนี้"
    })

    # UI
    return ft.View(
        route="/document",
        controls=[
            ft.AppBar(
                title=ft.Text("รายละเอียดเอกสาร"),
                bgcolor="#e91e63",
                center_title=True,
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/home")),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text(doc["title"], size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(f"สถานะ: {doc['status']}", size=14, color="green" if doc["status"] == "เสร็จสิ้น" else "orange"),
                    ft.Divider(height=20),
                    ft.Text(doc["description"], size=14),
                ],
                spacing=10),
                padding=20
            )
        ]
    )
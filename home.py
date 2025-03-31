import flet as ft

def HomeView(page: ft.Page):
    def go_profile(e):
        page.go("/profile")

    def go_document_detail(doc_id):
        def handler(e):
            page.client_storage.set("doc_id", doc_id)
            page.go("/document")
        return handler
    
    # mock ข้อมูลเอกสาร
    documents = [
        {"id": "001", "title": "ขอสอบประมวลความรู้ / ใบคำร้องขอสอบปลายภาค", "status": "รอดำเนินการ"},
        {"id": "002", "title": "ขอสอบวิทยานิพนธ์ / รับรองหัวข้อวิทยานิพนธ์", "status": "เสร็จสิ้น"},
        {"id": "003", "title": "ขออนุมัติเค้าโครง / แจ้งชื่อกรรมการสอบเค้าโครง", "status": "รอดำเนินการ"},
        {"id": "004", "title": "ขอเปลี่ยนกรรมการ / กรรมการไม่สามารถเข้าร่วมได้", "status": "รอดำเนินการ"},
        {"id": "005", "title": "ขอสอบวิทยานิพนธ์ / ขออนุมัติสอบ", "status": "รอดำเนินการ"},
        {"id": "006", "title": "ขอเลื่อนสอบ / ยื่นแบบฟอร์มขอเลื่อนสอบ", "status": "รอดำเนินการ"},
    ]

    # สร้างการ์ดเอกสาร
    cards = []
    for doc in documents:
        card = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        width=50,
                        height=50,
                        bgcolor="#e0e0e0",
                        border_radius=8,
                        alignment=ft.alignment.center,
                        content=ft.Text("📄")
                    ),
                    ft.Text(doc["title"], size=14, weight=ft.FontWeight.W_500),
                ], alignment=ft.MainAxisAlignment.START, spacing=10),
                ft.Row([
                    ft.Row([
                        ft.Icon(name=ft.icons.CHECK_CIRCLE, color="green", size=16),
                        ft.Text(doc["status"], size=12),
                    ]),
                    ft.Icon(name=ft.icons.PEOPLE, size=16),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.ElevatedButton(
                    text="ดูรายละเอียด",
                    bgcolor="#e91e63",
                    color="white",
                    on_click=go_document_detail(doc["id"]),
                    height=32,
                    style=ft.ButtonStyle(padding=10, shape=ft.RoundedRectangleBorder(radius=6))
                )
            ],
            spacing=5),
            padding=10,
            margin=10,
            bgcolor="white",
            border_radius=10,
            shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.GREY_300)
        )
        cards.append(card)

    # TopBar
    topbar = ft.Container(
        bgcolor="#2f2f2f",
        padding=10,
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.icons.ACCOUNT_CIRCLE, icon_color="#e91e63", icon_size=30, on_click=go_profile),
                ft.Container(
                    content=ft.Image(src="assets/logo.png", width=50),
                    expand=True,
                    alignment=ft.alignment.center
                ),
                ft.IconButton(icon=ft.icons.LOGOUT, icon_color="#e91e63", on_click=lambda _: page.go("/"))
            ]),
            ft.TextField(
                hint_text="Search",
                prefix_icon=ft.icons.SEARCH,
                border_radius=10,
                filled=True,
                fill_color="#cfcfcf",
                height=40,
            )
        ],
        spacing=10)
    )

    # Bottom Navigation
    nav_bar = ft.Container(
        bgcolor="white",
        padding=10,
        content=ft.Row([
            ft.Icon(name=ft.icons.CHAT, color="#e91e63"),
            ft.Icon(name=ft.icons.HOME, color="#e91e63"),
            ft.Icon(name=ft.icons.NOTIFICATIONS, color="#e91e63"),
            ft.Icon(name=ft.icons.PERSON, color="#e91e63"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND)
    )

    return ft.View(
        route="/home",
        controls=[
            topbar,
            ft.Column(cards, scroll=ft.ScrollMode.AUTO, expand=True),
            nav_bar
        ],
        bgcolor="#f9f9f9"
    )

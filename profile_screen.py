import flet as ft

def ProfileView(page: ft.Page):
    student_id = page.client_storage.get("student_id") or "65030226"

    mock_profiles = {
        "65030226": {
            "id": "65030226",
            "user_type": "Student",
            "name_en": "Watcharakorn Noipandee",
            "name_th": "วัชรากร น้อยพันธ์ดี",
            "admission_year": "2565",
            "term": "1",
            "status": "out of condition",
            "semester": "2",
            "year": "2570",
            "plan": "-",
            "admission_type": "-",
            "course": "-"
        }
    }

    user = mock_profiles.get(student_id)

    return ft.View(
        route="/profile",
        controls=[
            ft.AppBar(
                title=ft.Text("ข้อมูลส่วนตัว"),
                bgcolor="#e91e63",
                center_title=True,
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/home")),
            ),
            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    [
                        ft.Row([
                            ft.CircleAvatar(radius=40, bgcolor="#f8bbd0"),
                            ft.IconButton(icon=ft.icons.LOGOUT, icon_color="red", on_click=lambda _: page.go("/"))
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text("Profile", size=20, weight=ft.FontWeight.BOLD),
                        ft.TextField(label="ID", value=user["id"], read_only=True),
                        ft.TextField(label="User Type", value=user["user_type"], read_only=True),
                        ft.TextField(label="Name (EN)", value=user["name_en"], read_only=True),
                        ft.TextField(label="Name (TH)", value=user["name_th"], read_only=True),
                        ft.TextField(label="Year of admission", value=user["admission_year"], read_only=True),
                        ft.TextField(label="Term", value=user["term"], read_only=True),
                        ft.TextField(label="Education plan", value=user["plan"], read_only=True),
                        ft.TextField(label="Admission type", value=user["admission_type"], read_only=True),
                        ft.TextField(label="Student status", value=user["status"], read_only=True),
                        ft.TextField(label="Semester", value=user["semester"], read_only=True),
                        ft.TextField(label="Year", value=user["year"], read_only=True),
                        ft.TextField(label="Course", value=user["course"], read_only=True),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                )
            )
        ]
    )
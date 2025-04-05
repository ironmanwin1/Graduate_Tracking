
import flet as ft
import httpx

class ProfileView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/profile")
        self.page = page
        student = self.get_logged_in_student()

        def label_box(title, value, color="#ed4988"):
            return ft.Column([
                ft.Text(title, size=12),
                ft.Container(
                    content=ft.Text(value, color=color, weight="bold"),
                    padding=ft.padding.symmetric(horizontal=12, vertical=6),
                    border=ft.border.all(1, color),
                    border_radius=8
                )
            ], spacing=2, width=300)

        if not student:
            self.controls = [
                ft.Text("ไม่พบนักศึกษา", color="red", size=20)
            ]
            return

        # Profile picture
        profile_pic = ft.Stack([
            ft.CircleAvatar(bgcolor="#f8a7c6", radius=50),
            ft.Container(
                content=ft.Icon(ft.icons.EDIT, size=16),
                alignment=ft.alignment.bottom_right,
                padding=5
            )
        ])

        logout_btn = ft.IconButton(
            icon=ft.icons.LOGOUT,
            icon_color="#ed4988",
            on_click=lambda _: self.page.go("/")
        )

        responsive_content = ft.ResponsiveRow([
            ft.Container(content=ft.Text("ข้อมูลส่วนตัว", size=12, color=ft.colors.GREY), col={"xs": 12}),
            ft.Container(
                content=ft.Row([profile_pic, logout_btn], alignment="spaceBetween"),
                col={"xs": 12, "sm": 12}
            ),
            ft.Container(content=ft.Text("Profile", size=18, weight="bold", color="#ed4988"), col={"xs": 12}),
            ft.Container(content=ft.Row([
                label_box("ID", student["student_id"]),
                label_box("User Type", "Student")
            ], wrap=True), col={"xs": 12}),
            ft.Container(content=label_box("Name (EN)", student["name"]), col={"xs": 12}),
            ft.Container(content=label_box("Name (TH)", student.get("name_th", "-")), col={"xs": 12}),
            ft.Container(content=ft.Row([
                label_box("Year of admission", str(student.get("year", "-"))),
                label_box("Term of admission", str(student.get("semester", "-")))
            ], wrap=True), col={"xs": 12}),
            ft.Container(content=ft.Row([
                label_box("Education plan", student.get("study_plan", "-")),
                label_box("Admission type", "-")
            ], wrap=True), col={"xs": 12}),
            ft.Container(content=label_box("Student status", student.get("status", "-"), color="#d63384"), col={"xs": 12}),
            ft.Container(content=ft.Row([
                label_box("Semester", str(student.get("semester", "-"))),
                label_box("Year", str(student.get("year", "-")))
            ], wrap=True), col={"xs": 12}),
            ft.Container(content=label_box("Course", "-"), col={"xs": 12}),
        ], spacing=10, run_spacing=10)

        scrollable_container = ft.Container(
            content=ft.Column([responsive_content], scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=10
        )

        bottom_bar = ft.Row([
            ft.IconButton(icon=ft.icons.CHAT, icon_color="#ed4988", on_click=lambda _: self.page.go("/contact")),
            ft.IconButton(icon=ft.icons.HOME, icon_color="#ed4988", on_click=lambda _: self.page.go("/home")),
            ft.IconButton(icon=ft.icons.NOTIFICATIONS, icon_color="#ed4988")
        ], alignment="spaceEvenly", height=60)

        self.controls = [
            scrollable_container,
            bottom_bar
        ]

    def get_logged_in_student(self):
        student_id = self.page.client_storage.get("student_id")
        print("📦 student_id from storage:", student_id)

        if not student_id:
            return None

        try:
            res = httpx.get(f"http://127.0.0.1:8000/api/student/{student_id}")
            print("📡 API Status:", res.status_code)
            print("📡 API Response:", res.json())
            if res.status_code == 200 and "student_id" in res.json():
                return res.json()
        except Exception as e:
            print("❌ Error connecting to API:", e)

        return None

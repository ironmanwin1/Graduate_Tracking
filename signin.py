import flet as ft
import json

class SignInView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/")
        self.page = page
        self.page.bgcolor = "#f2f2f2"

        # Input Fields
        self.username = ft.TextField(
            hint_text="Username",
            prefix_icon=ft.icons.PERSON,
            bgcolor="#e0e0e0",
            border_radius=10,
            border=ft.InputBorder.NONE,
            width=300,
        )
        self.password = ft.TextField(
            hint_text="Password",
            prefix_icon=ft.icons.VPN_KEY,
            password=True,
            can_reveal_password=True,
            bgcolor="#e0e0e0",
            border_radius=10,
            border=ft.InputBorder.NONE,
            width=300,
        )
        self.error_text = ft.Text(color="red")

        # Header Logo
        header = ft.Container(
            bgcolor="#f8a7c6",
            content=ft.Row([
                ft.Image(src="/Users/watcharakorn/Desktop/grad_tracking_app/assets/logosingin.png", height=40),
            ], alignment="center", spacing=10),
            padding=20,
        )

        # Main Login Card
        login_card = ft.Container(
            bgcolor="#ed4988",
            border_radius=30,
            padding=30,
            content=ft.Container(
                bgcolor="white",
                border_radius=20,
                padding=25,
                content=ft.Column([
                    ft.Text("ยืนยันตัวตนด้วยบริการของสถาบันฯ", weight="bold", size=16),
                    ft.Text("โดยใช้ E-mail Account ของสถาบันฯ", size=14, color=ft.colors.BLUE_GREY),
                    self.username,
                    self.password,
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Next",
                            on_click=self.sign_in,
                            bgcolor="#f8a7c6",
                            color="white",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=20
                            )
                        ),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=10)
                    ),
                    self.error_text
                ],
                horizontal_alignment="center",
                spacing=15),
            )
        )

        self.controls = [
            ft.Column([
                header,
                login_card
            ],
            horizontal_alignment="center",
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=40
            )
        ]

    def sign_in(self, e):
        email = self.username.value.strip()
        password = self.password.value.strip()
        try:
            with open("mock_data/student.json", "r", encoding="utf-8") as f:
                students = json.load(f)
        except:
            self.error_text.value = "ไม่สามารถโหลดข้อมูลนักศึกษาได้"
            self.page.update()
            return

        for student in students:
            if student["email"] == email and password == "1234":
                self.page.client_storage.set("student_id", student["student_id"])
                self.page.go("/home")
                return

        self.error_text.value = "อีเมลหรือรหัสผ่านไม่ถูกต้อง"
        self.page.update()

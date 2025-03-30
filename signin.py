import flet as ft
import json

class SignInView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/")
        self.page = page
        self.username = ft.TextField(label="อีเมล", autofocus=True, width=300)
        self.password = ft.TextField(label="รหัสผ่าน", password=True, can_reveal_password=True, width=300)
        self.error_text = ft.Text(color="red")
        self.controls = [
            ft.Column([
                ft.Text("ระบบติดตามนักศึกษาบัณฑิตศึกษา", size=24, weight="bold"),
                self.username,
                self.password,
                ft.ElevatedButton(text="เข้าสู่ระบบ", on_click=self.sign_in),
                self.error_text,
            ], horizontal_alignment="center", alignment=ft.MainAxisAlignment.CENTER, spacing=20)
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

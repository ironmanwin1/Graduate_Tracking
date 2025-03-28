
import flet as ft

def SignInView(page: ft.Page):
    # Here you can display some content for authentication
    title = ft.Text("Authentication", size=30, color="#e91e63")
    page.add(title)

    # โลโก้
    logo = ft.Image(src="assets/logo.png", width=150)

    # หัวบาร์สีชมพู + โลโก้ด้านใน
    header_bar = ft.Container(
        bgcolor="#f5a1c4",
        height=100,
        alignment=ft.alignment.center,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[logo]
        )
    )

    # กล่อง Sign In
    title_text = ft.Text("ยืนยันตัวตนด้วยบริการของสถาบันฯ", weight=ft.FontWeight.BOLD, size=16)
    subtitle_text = ft.Text("โดยใช้ E-mail Account ของสถาบันฯ", size=12)

    username_field = ft.TextField(label="Username", border_radius=10, filled=True)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, border_radius=10, filled=True)

    def on_login(e):
        student_id = username_field.value.strip()
        if student_id:
            page.client_storage.set("student_id", student_id)
            page.go("/home")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("กรุณากรอก Student ID"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    sign_in_button = ft.ElevatedButton(
        text="Next",
        bgcolor="#f5a1c4",
        color="white",
        width=100,
        on_click=on_login
    )

    card = ft.Container(
        padding=20,
        bgcolor="#e91e63",
        border_radius=20,
        content=ft.Column(
            controls=[
                title_text,
                subtitle_text,
                username_field,
                password_field,
                sign_in_button
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    return ft.Column(
        expand=True,
        controls=[
            header_bar,
            ft.Container(
                expand=True,
                alignment=ft.alignment.top_center,
                content=card,
                padding=30
            )
        ]
    )

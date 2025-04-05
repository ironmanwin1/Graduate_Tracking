import flet as ft

class ContactView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/contact")
        self.page = page

        def section_title(text):
            return ft.Text(text, size=16, weight="bold", text_align="center")

        def pink_box(content):
            return ft.Container(
                content=content,
                bgcolor="#f8a7c6",
                border_radius=20,
                padding=20,
                alignment=ft.alignment.center,
                expand=True
            )

        self.controls = [
            ft.Container(
                bgcolor="#2c2c2c",
                padding=20,
                content=ft.Row([
                    ft.IconButton(icon=ft.icons.ACCOUNT_CIRCLE, icon_color="#ed4988", icon_size=30, on_click=lambda _: page.go("/profile")),
                    ft.Image(src="/Users/watcharakorn/Desktop/grad_tracking_app/assets/logo1.png", height=50),
                    ft.IconButton(icon=ft.icons.LOGOUT, icon_color="#ed4988", on_click=lambda _: page.go("/"))
                ], alignment="spaceBetween")
            ),
            ft.Container(
                alignment=ft.alignment.center,
                padding=10,
                content=ft.ElevatedButton(
                    text="ติดต่อ/สอบถามเจ้าหน้าที่",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=20,
                        side=ft.BorderSide(width=1, color="#ed4988"),
                        bgcolor="white",
                        color="#000000"
                    )
                )
            ),
            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column([
                    section_title("ติดต่อช่องทาง Line"),
                    pink_box(ft.Image(src="assets/qr_line.png", width=200)),
                    ft.Divider(height=30, color="transparent"),
                    section_title("เบอร์ติดต่อช่องทาง"),
                    pink_box(
                        ft.Column([
                            ft.Text("093-6xx-5xx6", size=20, weight="bold"),
                            ft.Text("093-xxx-45xx", size=20, weight="bold")
                        ], horizontal_alignment="center")
                    )
                ],
                horizontal_alignment="center",
                scroll=ft.ScrollMode.AUTO)
            ),
            ft.Row([
                ft.IconButton(icon=ft.icons.CHAT, icon_color="#ed4988", on_click=lambda _: page.go("/contact")),
                ft.IconButton(icon=ft.icons.HOME, icon_color="#ed4988", on_click=lambda _: page.go("/home")),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS, icon_color="#ed4988")
            ], alignment="spaceEvenly", height=60)
        ]

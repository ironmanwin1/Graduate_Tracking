import flet as ft
from document_detail import DocumentDetailView
from home import HomeView
from signin import SignInView
from profile_screen import ProfileView



def main(page: ft.Page):
    page.title = "Graduate Tracking App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(SignInView(page))
        elif page.route == "/profile":
            page.views.append(ProfileView(page))
            page.update()
        elif page.route == "/document":
            page.views.append(DocumentDetailView(page))
        elif page.route == "/home":
            page.views.append(HomeView(page))

        page.update()

    page.on_route_change = route_change
    route_change(page.route)

ft.app(target=main, view=ft.WEB_BROWSER)
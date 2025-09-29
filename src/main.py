import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.template_route import TemplateRoute
from flet.core.theme import PageTransitionTheme

from views.base import Router, View


async def main(page: ft.Page):
    page.title = "Routes Example"

    router = Router([
        View(route="explore", label="Explore", icon=ft.Icons.EXPLORE),
        View(route="search", label="Search", icon=ft.Icons.SEARCH),
        View(route="recipies", label="Recipies", icon=ft.Icons.BOOKMARK_BORDER, icon_selected=ft.Icons.BOOKMARK),
        View(route="profile", label="Profile", icon=ft.Icons.FACE),
    ])


    def route_change(route):
        t_route = TemplateRoute(page.route)

        page.views.clear()
        page.views.append(ft.View(
            "/",
            [
                ft.ElevatedButton("Dashboard", on_click=lambda _: page.go("/dashboard")),
            ],
            navigation_bar=router.navigation
        ))
        if page.route == "/dashboard":
            page.views.append(ft.View(
                "/dashboard",
                [
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ],
                navigation_bar=router.navigation
            ))
        if t_route.match("/recipe/:id"):
            page.views.append(ft.View(
                "/recipe/:id",
                [
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ],
                navigation_bar=router.navigation
            ))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=PageTransitionTheme.OPEN_UPWARDS,
            ios=PageTransitionTheme.CUPERTINO,
            macos=PageTransitionTheme.NONE,
            linux=PageTransitionTheme.NONE,
            windows=PageTransitionTheme.NONE,
        )
    )
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


ft.app(main)
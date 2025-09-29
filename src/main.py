import asyncio

import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.template_route import TemplateRoute
from flet.core.theme import PageTransitionTheme


async def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        t_route = TemplateRoute(page.route)

        def navigation_change(e: ControlEvent):
            next_index = int(e.data)
            next_route = list(nav_destinations.keys())[next_index]
            page.go(f"/{next_route}")
            page.update()

        nav_destinations = {
            "explore": ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            "search": ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            "recipies": ft.NavigationBarDestination(
                    icon=ft.Icons.BOOKMARK_BORDER,
                    selected_icon=ft.Icons.BOOKMARK,
                    label="Recipies",
                ),
            "profile": ft.NavigationBarDestination(
                    icon=ft.Icons.FACE,
                    label="Profile",
                ),
        }
        nav = ft.NavigationBar(
            destinations=list(nav_destinations.values()),
            on_change=navigation_change,
        )

        page.views.clear()
        page.views.append(ft.View(
            "/",
            [
                ft.ElevatedButton("Dashboard", on_click=lambda _: page.go("/dashboard")),
            ],
            navigation_bar=nav
        ))
        if page.route == "/dashboard":
            page.views.append(ft.View(
                "/dashboard",
                [
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ],
                navigation_bar=nav
            ))
        if t_route.match("/recipe/:id"):
            page.views.append(ft.View(
                "/recipe/:id",
                [
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ],
                navigation_bar=nav
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
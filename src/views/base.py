from typing import Optional, Iterable, Sequence, List, Generator

import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.icons import Icons


class View:

    def __init__(self, route: str, label: str, icon: Icons, icon_selected: Optional[Icons] = None):
        self.route = route
        self.icon = icon
        self.icon_selected = icon_selected
        self.label = label

class Router:

    def __init__(self, views: Sequence[View]):
        self.views = views
        self.selected_view: Optional[View] = None

    def _navigation_destinations(self) -> Generator[ft.NavigationBarDestination, None, None]:
        for view in self.views:
            yield ft.NavigationBarDestination(label=view.label, icon=view.icon, selected_icon=view.icon_selected)

    def _navigation_change(self, event: ControlEvent):
        print("Navigation Change Event:", event)
        view_index = int(event.data)
        view = self.views[view_index]
        self.selected_view = view
        event.page.go(f"/{view.route}")

    def _get_selected_view_index(self) -> int:
        if self.selected_view is None:
            return 0
        return self.views.index(self.selected_view)

    @property
    def navigation(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            destinations=list(self._navigation_destinations()),
            on_change=self._navigation_change,
            selected_index=self._get_selected_view_index()
        )
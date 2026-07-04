import reflex as rx
from app.states.navigation import NavigationState


def nav_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        href=href,
        class_name="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors duration-200 focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400 rounded-md px-1 py-0.5",
    )


def mobile_nav_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        href=href,
        on_click=NavigationState.close_mobile_menu,
        class_name="text-base font-semibold text-gray-800 hover:text-blue-600 py-2 border-b border-gray-100 w-full block transition-colors duration-200",
    )


def navigation() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            # Logo
            rx.el.a(
                rx.el.div(
                    rx.icon("compass", class_name="h-6 w-6 text-blue-600"),
                    rx.el.span(
                        "CareerPilot AI",
                        class_name="text-xl font-bold text-gray-900 tracking-tight",
                    ),
                    class_name="flex items-center gap-2",
                ),
                href="/",
                class_name="flex items-center",
            ),
            # Desktop navigation links
            rx.el.nav(
                nav_link("Home", "/"),
                nav_link("About AI Engine", "/about"),
                nav_link("Dashboard Preview", "/dashboard"),
                class_name="hidden md:flex items-center gap-8",
            ),
            # CTA Buttons
            rx.el.div(
                rx.el.a(
                    "Launch App",
                    href="/dashboard",
                    class_name="bg-blue-600 hover:bg-blue-700 text-white font-medium px-4 py-2 rounded-xl text-sm transition-all duration-200 shadow-xs hover:shadow-sm flex items-center gap-1.5",
                ),
                class_name="hidden md:flex items-center gap-4",
            ),
            # Mobile Menu Toggle
            rx.el.button(
                rx.cond(
                    NavigationState.mobile_menu_open,
                    rx.icon("x", class_name="h-6 w-6 text-gray-700"),
                    rx.icon("menu", class_name="h-6 w-6 text-gray-700"),
                ),
                on_click=NavigationState.toggle_mobile_menu,
                class_name="md:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400",
                aria_label="Toggle menu",
                aria_expanded=NavigationState.mobile_menu_open,
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between",
        ),
        # Mobile Menu Drawer
        rx.cond(
            NavigationState.mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    mobile_nav_link("Home", "/"),
                    mobile_nav_link("About AI Engine", "/about"),
                    mobile_nav_link("Dashboard Preview", "/dashboard"),
                    rx.el.div(
                        rx.el.a(
                            "Launch App",
                            href="/dashboard",
                            on_click=NavigationState.close_mobile_menu,
                            class_name="w-full text-center bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl block shadow-sm mt-4",
                        ),
                        class_name="pt-4",
                    ),
                    class_name="flex flex-col gap-4 p-4 bg-white border-b border-gray-200 shadow-lg",
                ),
                class_name="md:hidden absolute top-16 left-0 right-0 z-50 animate-fade-in",
            ),
            None,
        ),
        class_name="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-gray-100 w-full",
    )

import reflex as rx
from app.components.navigation import navigation
from app.components.footer import footer
from app.states.career import CareerState


class SidebarState(rx.State):
    @rx.var
    def current_path(self) -> str:
        return self.router.page.path


def sidebar_link(label: str, href: str, icon: str) -> rx.Component:
    is_active = SidebarState.current_path == href
    return rx.el.a(
        rx.icon(icon, class_name="h-4 w-4 shrink-0"),
        rx.el.span(label, class_name="text-sm font-semibold"),
        href=href,
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 px-3 py-2.5 rounded-xl text-blue-700 bg-blue-50 border border-blue-100 transition-colors focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400",
            "flex items-center gap-3 px-3 py-2.5 rounded-xl text-gray-600 hover:bg-blue-50 hover:text-blue-700 transition-colors focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400 border border-transparent",
        ),
    )


def dashboard_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "CareerPilot",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-3",
                ),
                sidebar_link("Overview", "/dashboard", "layout-dashboard"),
                sidebar_link(
                    "Resume Analysis", "/dashboard/resume", "file-text"
                ),
                sidebar_link("Skill Gap", "/dashboard/skill-gap", "target"),
                sidebar_link("AI Roadmap", "/dashboard/roadmap", "map"),
                class_name="flex flex-col gap-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Target Role",
                        class_name="text-xs font-semibold text-gray-500 mb-1",
                    ),
                    rx.el.p(
                        CareerState.role["name"],
                        class_name="text-sm font-bold text-gray-900",
                    ),
                    class_name="mb-3",
                ),
                rx.el.div(
                    rx.el.p(
                        "Resume",
                        class_name="text-xs font-semibold text-gray-500 mb-1",
                    ),
                    rx.cond(
                        CareerState.has_resume,
                        rx.el.p(
                            CareerState.resume_filename,
                            class_name="text-xs font-medium text-green-700 truncate",
                        ),
                        rx.el.p(
                            "Not uploaded",
                            class_name="text-xs font-medium text-gray-400",
                        ),
                    ),
                ),
                class_name="mt-8 p-4 bg-blue-50/50 border border-blue-100 rounded-xl",
            ),
            class_name="p-6 sticky top-16",
        ),
        class_name="w-64 shrink-0 border-r border-gray-100 bg-white hidden lg:block",
        aria_label="Dashboard navigation",
    )


def dashboard_mobile_nav() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.a(
                rx.icon("layout-dashboard", class_name="h-4 w-4"),
                "Overview",
                href="/dashboard",
                class_name="flex items-center gap-1.5 px-3 py-2 text-xs font-semibold text-gray-600 hover:text-blue-700 whitespace-nowrap rounded-lg",
            ),
            rx.el.a(
                rx.icon("file-text", class_name="h-4 w-4"),
                "Resume",
                href="/dashboard/resume",
                class_name="flex items-center gap-1.5 px-3 py-2 text-xs font-semibold text-gray-600 hover:text-blue-700 whitespace-nowrap rounded-lg",
            ),
            rx.el.a(
                rx.icon("target", class_name="h-4 w-4"),
                "Skill Gap",
                href="/dashboard/skill-gap",
                class_name="flex items-center gap-1.5 px-3 py-2 text-xs font-semibold text-gray-600 hover:text-blue-700 whitespace-nowrap rounded-lg",
            ),
            rx.el.a(
                rx.icon("map", class_name="h-4 w-4"),
                "Roadmap",
                href="/dashboard/roadmap",
                class_name="flex items-center gap-1.5 px-3 py-2 text-xs font-semibold text-gray-600 hover:text-blue-700 whitespace-nowrap rounded-lg",
            ),
            class_name="flex items-center gap-1 overflow-x-auto",
        ),
        class_name="lg:hidden bg-white border-b border-gray-100 px-4 py-2",
        aria_label="Dashboard navigation",
    )


def dashboard_layout(*content: rx.Component) -> rx.Component:
    return rx.el.main(
        navigation(),
        dashboard_mobile_nav(),
        rx.el.div(
            dashboard_sidebar(),
            rx.el.div(
                rx.el.div(
                    *content,
                    class_name="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8",
                ),
                class_name="flex-1 min-w-0",
            ),
            class_name="flex bg-slate-50/40 min-h-[calc(100vh-8rem)]",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col justify-between",
    )

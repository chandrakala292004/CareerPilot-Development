import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("compass", class_name="h-6 w-6 text-blue-600"),
                        rx.el.span(
                            "CareerPilot AI",
                            class_name="text-lg font-bold text-gray-900 tracking-tight",
                        ),
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        "Autonomous career intelligence providing resume optimization, skill gap auditing, and tailored career pathways powered by advanced AI.",
                        class_name="text-sm text-gray-500 max-w-sm font-medium",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.h4(
                        "Platform",
                        class_name="text-sm font-semibold text-gray-900 mb-3 uppercase tracking-wider",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "Features",
                                href="/#features",
                                class_name="text-sm text-gray-500 hover:text-blue-600 font-medium",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "How It Works",
                                href="/#how-it-works",
                                class_name="text-sm text-gray-500 hover:text-blue-600 font-medium",
                            ),
                            class_name="mt-2",
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Dashboard",
                                href="/dashboard",
                                class_name="text-sm text-gray-500 hover:text-blue-600 font-medium",
                            ),
                            class_name="mt-2",
                        ),
                        class_name="list-none p-0 m-0",
                    ),
                ),
                rx.el.div(
                    rx.el.h4(
                        "Company",
                        class_name="text-sm font-semibold text-gray-900 mb-3 uppercase tracking-wider",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "About",
                                href="/about",
                                class_name="text-sm text-gray-500 hover:text-blue-600 font-medium",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Workflow",
                                href="/about#workflow",
                                class_name="text-sm text-gray-500 hover:text-blue-600 font-medium",
                            ),
                            class_name="mt-2",
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Privacy Policy",
                                href="/about#privacy",
                                class_name="text-sm text-gray-500 hover:text-blue-600 font-medium",
                            ),
                            class_name="mt-2",
                        ),
                        class_name="list-none p-0 m-0",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-4 gap-8 md:gap-12",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2025 CareerPilot AI. All rights reserved. Built to pilot your career dynamically with secure LLMs.",
                    class_name="text-xs text-gray-400 font-medium text-center",
                ),
                class_name="mt-8 pt-8 border-t border-gray-100 flex justify-center items-center",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gray-50 border-t border-gray-100 w-full",
    )

import reflex as rx
from app.states.career import CareerState


def role_card(role: dict) -> rx.Component:
    is_selected = CareerState.selected_role_id == role["id"]
    return rx.el.button(
        rx.el.div(
            rx.icon(
                role["icon"],
                class_name=rx.cond(
                    is_selected,
                    "h-5 w-5 text-blue-600",
                    "h-5 w-5 text-gray-500",
                ),
            ),
            class_name=rx.cond(
                is_selected,
                "size-10 rounded-xl bg-blue-100 flex items-center justify-center mb-3",
                "size-10 rounded-xl bg-gray-100 flex items-center justify-center mb-3",
            ),
        ),
        rx.el.p(
            role["name"],
            class_name="text-sm font-semibold text-gray-900 text-left",
        ),
        on_click=lambda: CareerState.set_role(role["id"]),
        type="button",
        aria_label=f"Select {role['name']} as target role",
        class_name=rx.cond(
            is_selected,
            "flex flex-col items-start p-4 rounded-2xl border-2 border-blue-500 bg-blue-50/40 shadow-sm transition-all focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400",
            "flex flex-col items-start p-4 rounded-2xl border border-gray-200 bg-white hover:border-blue-300 hover:shadow-xs transition-all focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400",
        ),
    )


def role_selector() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Select Target Role",
                class_name="text-lg font-bold text-gray-900",
            ),
            rx.el.p(
                "Choose the discipline you're transitioning toward.",
                class_name="text-sm text-gray-500 font-medium mt-1",
            ),
            class_name="mb-5",
        ),
        rx.el.div(
            rx.foreach(CareerState.role_options, role_card),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
    )

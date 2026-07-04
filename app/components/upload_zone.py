import reflex as rx
from app.states.career import CareerState
from app.states.ai_analysis import AIAnalysisState

UPLOAD_ID = "resume_upload"


def upload_zone() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Upload Resume", class_name="text-lg font-bold text-gray-900"
            ),
            rx.el.p(
                "PDF or TXT · max 5MB · text-based content only",
                class_name="text-sm text-gray-500 font-medium mt-1",
            ),
            class_name="mb-5",
        ),
        rx.cond(
            CareerState.has_resume,
            # Uploaded state
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "file-check-2", class_name="h-6 w-6 text-green-600"
                        ),
                        class_name="size-12 rounded-xl bg-green-50 flex items-center justify-center shrink-0",
                    ),
                    rx.el.div(
                        rx.el.p(
                            CareerState.resume_filename,
                            class_name="text-sm font-bold text-gray-900 truncate",
                        ),
                        rx.el.p(
                            f"{CareerState.resume_word_count} words · {CareerState.resume_char_count} chars extracted",
                            class_name="text-xs text-gray-500 font-medium mt-0.5",
                        ),
                        class_name="min-w-0 flex-1",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-4 w-4"),
                        on_click=[
                            CareerState.clear_resume,
                            AIAnalysisState.clear_analysis,
                        ],
                        type="button",
                        class_name="p-2 rounded-lg hover:bg-gray-100 text-gray-500 transition-colors focus:outline-hidden focus-visible:ring-2 focus-visible:ring-blue-400",
                        aria_label="Remove resume",
                    ),
                    class_name="flex items-center gap-4 p-4 bg-green-50/40 border border-green-100 rounded-xl",
                ),
                rx.el.div(
                    rx.el.p(
                        "Detected Skills",
                        class_name="text-xs font-semibold text-gray-600 mb-2 mt-4",
                    ),
                    rx.cond(
                        CareerState.detected_skills.length() > 0,
                        rx.el.div(
                            rx.foreach(
                                CareerState.detected_skills,
                                lambda s: rx.el.span(
                                    s,
                                    class_name="px-2.5 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                                ),
                            ),
                            class_name="flex flex-wrap gap-1.5",
                        ),
                        rx.el.p(
                            "No known skills detected in the resume text.",
                            class_name="text-xs text-gray-500 font-medium",
                        ),
                    ),
                ),
            ),
            # Empty state
            rx.el.div(
                rx.upload.root(
                    rx.el.div(
                        rx.icon(
                            "cloud-upload",
                            class_name="h-8 w-8 text-blue-500 mb-2",
                        ),
                        rx.el.p(
                            "Drop your resume here or click to browse",
                            class_name="text-sm font-semibold text-gray-700",
                        ),
                        rx.el.p(
                            "PDF or TXT · up to 5MB",
                            class_name="text-xs text-gray-400 font-medium mt-1",
                        ),
                        class_name="flex flex-col items-center justify-center p-8 border-2 border-dashed border-gray-200 bg-slate-50/40 rounded-xl cursor-pointer hover:border-blue-400 hover:bg-blue-50/30 transition-colors",
                    ),
                    id=UPLOAD_ID,
                    accept={
                        "application/pdf": [".pdf"],
                        "text/plain": [".txt"],
                    },
                    max_files=1,
                    max_size=5 * 1024 * 1024,
                    on_drop=CareerState.handle_upload(
                        rx.upload_files(
                            upload_id=UPLOAD_ID,
                            on_upload_progress=CareerState.handle_upload_progress,
                        )
                    ),
                ),
                rx.cond(
                    CareerState.is_extracting,
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                class_name="h-2 bg-blue-500 rounded-full transition-all",
                                style={
                                    "width": f"{CareerState.upload_progress}%"
                                },
                            ),
                            class_name="w-full h-2 bg-gray-100 rounded-full overflow-hidden",
                        ),
                        rx.el.p(
                            f"Extracting resume text... {CareerState.upload_progress}%",
                            class_name="text-xs text-blue-700 font-semibold mt-2",
                        ),
                        class_name="mt-4",
                    ),
                    None,
                ),
                rx.cond(
                    CareerState.resume_error != "",
                    rx.el.div(
                        rx.icon(
                            "triangle-alert",
                            class_name="h-4 w-4 text-red-500 shrink-0",
                        ),
                        rx.el.p(
                            CareerState.resume_error,
                            class_name="text-xs text-red-700 font-semibold",
                        ),
                        class_name="flex items-center gap-2 p-3 bg-red-50 border border-red-100 rounded-xl mt-4",
                    ),
                    None,
                ),
            ),
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
    )

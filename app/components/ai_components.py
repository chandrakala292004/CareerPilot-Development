import reflex as rx
from app.states.ai_analysis import AIAnalysisState
from app.states.career import CareerState


def analysis_button(label: str = "Run AI Analysis") -> rx.Component:
    return rx.el.button(
        rx.cond(
            AIAnalysisState.is_analyzing,
            rx.icon("loader-circle", class_name="h-4 w-4 animate-spin"),
            rx.icon("wand-sparkles", class_name="h-4 w-4"),
        ),
        rx.cond(
            AIAnalysisState.is_analyzing,
            rx.el.span("Analyzing with Gemini..."),
            rx.el.span(label),
        ),
        on_click=AIAnalysisState.run_analysis,
        disabled=AIAnalysisState.is_analyzing | ~CareerState.has_resume,
        type="button",
        class_name=rx.cond(
            AIAnalysisState.is_analyzing | ~CareerState.has_resume,
            "inline-flex items-center gap-2 bg-blue-600 text-white text-sm font-semibold px-4 py-2.5 rounded-xl opacity-60 cursor-not-allowed",
            "inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-4 py-2.5 rounded-xl transition-colors shadow-xs",
        ),
    )


def retry_button() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("refresh-cw", class_name="h-4 w-4"),
            rx.el.span("Re-run"),
            on_click=AIAnalysisState.run_analysis,
            disabled=AIAnalysisState.is_analyzing,
            type="button",
            class_name="inline-flex items-center gap-2 bg-white/95 hover:bg-white text-blue-700 text-sm font-semibold px-4 py-2 rounded-xl transition-colors focus:outline-hidden focus-visible:ring-2 focus-visible:ring-white",
        ),
        rx.el.button(
            rx.icon("rotate-ccw", class_name="h-4 w-4"),
            rx.el.span("Reset"),
            on_click=AIAnalysisState.clear_analysis,
            disabled=AIAnalysisState.is_analyzing,
            type="button",
            class_name="inline-flex items-center gap-2 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold px-4 py-2 rounded-xl border border-white/30 transition-colors focus:outline-hidden focus-visible:ring-2 focus-visible:ring-white",
        ),
        class_name="flex items-center gap-2",
    )


def error_banner() -> rx.Component:
    return rx.cond(
        AIAnalysisState.analysis_error != "",
        rx.el.div(
            rx.icon(
                "triangle-alert",
                class_name="h-5 w-5 text-red-600 shrink-0 mt-0.5",
            ),
            rx.el.div(
                rx.el.p(
                    "AI Analysis Error",
                    class_name="text-sm font-bold text-red-800 mb-1",
                ),
                rx.el.p(
                    AIAnalysisState.analysis_error,
                    class_name="text-xs text-red-700 font-medium leading-relaxed",
                ),
                rx.el.button(
                    rx.icon("refresh-cw", class_name="h-3 w-3"),
                    "Retry",
                    on_click=AIAnalysisState.run_analysis,
                    disabled=AIAnalysisState.is_analyzing,
                    type="button",
                    class_name="mt-3 inline-flex items-center gap-1.5 bg-red-600 hover:bg-red-700 text-white text-xs font-semibold px-3 py-1.5 rounded-lg transition-colors",
                ),
                class_name="flex-1",
            ),
            class_name="flex items-start gap-3 p-4 bg-red-50 border border-red-100 rounded-2xl",
        ),
        rx.fragment(),
    )


def loading_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "loader-circle",
                class_name="h-6 w-6 text-blue-600 animate-spin",
            ),
            class_name="size-12 rounded-xl bg-blue-50 flex items-center justify-center mb-4",
        ),
        rx.el.h4(
            "Gemini is analyzing your resume...",
            class_name="text-base font-bold text-gray-900 mb-1",
        ),
        rx.el.p(
            "Auditing skill signals, mapping gaps, and generating your personalized 30-day roadmap. This usually takes 10-25 seconds.",
            class_name="text-sm text-gray-500 font-medium leading-relaxed mb-4",
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-2 bg-blue-500 rounded-full animate-pulse",
                style={"width": "70%"},
            ),
            class_name="w-full h-2 bg-gray-100 rounded-full overflow-hidden",
        ),
        class_name="bg-white p-6 rounded-2xl border border-blue-100 shadow-xs",
    )


def analysis_cta_panel(action_label: str = "Run AI Analysis") -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("sparkles", class_name="h-5 w-5 text-blue-600"),
            class_name="size-10 rounded-xl bg-blue-50 flex items-center justify-center mb-3",
        ),
        rx.el.h4(
            "Unlock AI Career Intelligence",
            class_name="text-base font-bold text-gray-900 mb-1",
        ),
        rx.el.p(
            "Send your resume and target role to Gemini 2.5 Flash. Get a readiness score, gap analysis with importance and learning time, ATS tips, a 30-day daily roadmap, certifications, projects, and personalized advice.",
            class_name="text-xs text-gray-500 font-medium leading-relaxed mb-4",
        ),
        analysis_button(action_label),
        rx.cond(
            ~CareerState.has_resume,
            rx.el.p(
                "Upload a resume to enable analysis.",
                class_name="text-[11px] text-gray-400 font-medium mt-2",
            ),
            rx.fragment(),
        ),
        error_banner(),
        class_name="bg-blue-50/30 border border-blue-100 rounded-2xl p-6 flex flex-col gap-2",
    )


def importance_badge(level: str) -> rx.Component:
    return rx.el.span(
        level,
        class_name=rx.match(
            level,
            (
                "High",
                "px-2 py-0.5 bg-red-50 text-red-700 text-[10px] font-bold rounded-md border border-red-100 uppercase tracking-wider",
            ),
            (
                "Medium",
                "px-2 py-0.5 bg-yellow-50 text-yellow-700 text-[10px] font-bold rounded-md border border-yellow-100 uppercase tracking-wider",
            ),
            (
                "Low",
                "px-2 py-0.5 bg-blue-50 text-blue-700 text-[10px] font-bold rounded-md border border-blue-100 uppercase tracking-wider",
            ),
            "px-2 py-0.5 bg-gray-50 text-gray-700 text-[10px] font-bold rounded-md border border-gray-100 uppercase tracking-wider",
        ),
    )


def missing_skill_row(item: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                item["skill"],
                class_name="text-sm font-bold text-gray-900",
            ),
            rx.el.div(
                importance_badge(item["importance"]),
                rx.el.span(
                    rx.icon("clock", class_name="h-3 w-3"),
                    item["estimated_learning_time"],
                    class_name="inline-flex items-center gap-1 text-[11px] font-semibold text-gray-500",
                ),
                class_name="flex items-center gap-2 mt-1.5",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.icon("arrow-right", class_name="h-4 w-4 text-gray-300"),
        class_name="flex items-center gap-4 p-4 bg-white border border-gray-100 rounded-xl hover:border-blue-200 transition-colors",
    )


def readiness_hero() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "AI Career Readiness",
                    class_name="text-xs font-semibold text-blue-100 uppercase tracking-wider",
                ),
                rx.el.div(
                    rx.el.span(
                        AIAnalysisState.career_readiness_score.to_string(),
                        class_name="text-6xl font-extrabold text-white tracking-tight",
                    ),
                    rx.el.span(
                        "%",
                        class_name="text-3xl font-bold text-blue-200 ml-1",
                    ),
                    class_name="mt-2",
                ),
                rx.el.p(
                    AIAnalysisState.readiness_label,
                    class_name="text-sm font-semibold text-blue-100 mt-1",
                ),
            ),
            rx.el.div(
                rx.icon("gauge", class_name="h-7 w-7 text-white"),
                class_name="size-14 rounded-2xl bg-white/15 flex items-center justify-center",
            ),
            class_name="flex justify-between items-start",
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-2.5 bg-white rounded-full transition-all",
                style={"width": f"{AIAnalysisState.career_readiness_score}%"},
            ),
            class_name="w-full h-2.5 bg-white/20 rounded-full overflow-hidden mt-6",
        ),
        rx.el.p(
            AIAnalysisState.score_explanation,
            class_name="text-sm text-blue-50 font-medium mt-4 leading-relaxed",
        ),
        rx.el.div(
            rx.el.p(
                f"Analyzed for: {AIAnalysisState.analyzed_role_name}",
                class_name="text-xs text-blue-100 font-semibold",
            ),
            retry_button(),
            class_name="flex items-center justify-between mt-6",
        ),
        class_name="bg-gradient-to-br from-blue-600 to-blue-700 p-6 rounded-2xl shadow-sm",
    )


def _list_card(
    title: str, icon: str, items: rx.Var, empty: str, color: str = "blue"
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-4 w-4 text-{color}-600"),
            rx.el.h3(title, class_name="text-lg font-bold text-gray-900"),
            class_name="flex items-center gap-2 mb-4",
        ),
        rx.cond(
            items.length() > 0,
            rx.el.ul(
                rx.foreach(
                    items,
                    lambda i: rx.el.li(
                        rx.icon(
                            "circle-check",
                            class_name=f"h-4 w-4 text-{color}-600 shrink-0 mt-0.5",
                        ),
                        rx.el.span(
                            i,
                            class_name="text-sm text-gray-700 font-medium leading-relaxed",
                        ),
                        class_name="flex items-start gap-3 py-2",
                    ),
                ),
                class_name="flex flex-col divide-y divide-gray-50",
            ),
            rx.el.p(empty, class_name="text-sm text-gray-500 font-medium"),
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
    )


def _pill_card(
    title: str, icon: str, items: rx.Var, empty: str, color: str = "blue"
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-4 w-4 text-{color}-600"),
            rx.el.h3(title, class_name="text-lg font-bold text-gray-900"),
            class_name="flex items-center gap-2 mb-4",
        ),
        rx.cond(
            items.length() > 0,
            rx.el.div(
                rx.foreach(
                    items,
                    lambda s: rx.el.span(
                        s,
                        class_name=f"px-2.5 py-1 bg-{color}-50 text-{color}-700 text-xs font-semibold rounded-lg border border-{color}-100",
                    ),
                ),
                class_name="flex flex-wrap gap-1.5",
            ),
            rx.el.p(empty, class_name="text-sm text-gray-500 font-medium"),
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
    )


def ai_resume_analysis() -> rx.Component:
    return rx.el.div(
        readiness_hero(),
        rx.el.div(
            _pill_card(
                "Existing Skills",
                "circle-check",
                AIAnalysisState.existing_skills,
                "No existing skills detected.",
                "green",
            ),
            _pill_card(
                "Technical Skills",
                "code",
                AIAnalysisState.technical_skills,
                "No technical skills detected.",
                "blue",
            ),
            _pill_card(
                "Soft Skills",
                "users",
                AIAnalysisState.soft_skills,
                "No soft skills detected.",
                "purple",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        rx.el.div(
            _list_card(
                "Strengths",
                "trending-up",
                AIAnalysisState.strengths,
                "No strengths listed.",
                "green",
            ),
            _list_card(
                "Weaknesses",
                "trending-down",
                AIAnalysisState.weaknesses,
                "No weaknesses listed.",
                "red",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("file-check", class_name="h-4 w-4 text-blue-600"),
                rx.el.h3(
                    "ATS Optimization Tips",
                    class_name="text-lg font-bold text-gray-900",
                ),
                class_name="flex items-center gap-2 mb-4",
            ),
            rx.el.ul(
                rx.foreach(
                    AIAnalysisState.ats_tips,
                    lambda t: rx.el.li(
                        rx.icon(
                            "circle_check",
                            class_name="h-4 w-4 text-blue-600 shrink-0 mt-0.5",
                        ),
                        rx.el.span(
                            t,
                            class_name="text-sm text-gray-700 font-medium leading-relaxed",
                        ),
                        class_name="flex items-start gap-3 py-2",
                    ),
                ),
                class_name="flex flex-col divide-y divide-gray-50",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("lightbulb", class_name="h-4 w-4 text-blue-600"),
                rx.el.h3(
                    "Final Career Advice",
                    class_name="text-lg font-bold text-gray-900",
                ),
                class_name="flex items-center gap-2 mb-3",
            ),
            rx.el.p(
                AIAnalysisState.final_career_advice,
                class_name="text-sm text-gray-700 font-medium leading-relaxed",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
        ),
        class_name="flex flex-col gap-6",
    )


def ai_skill_gap() -> rx.Component:
    return rx.el.div(
        readiness_hero(),
        rx.el.div(
            rx.el.div(
                rx.icon("circle-alert", class_name="h-4 w-4 text-red-600"),
                rx.el.h3(
                    "Missing Skills to Learn",
                    class_name="text-lg font-bold text-gray-900",
                ),
                rx.el.span(
                    AIAnalysisState.missing_skills.length().to_string(),
                    class_name="ml-auto px-2 py-0.5 bg-red-50 text-red-700 text-xs font-bold rounded-md border border-red-100",
                ),
                class_name="flex items-center gap-2 mb-4",
            ),
            rx.cond(
                AIAnalysisState.missing_skills.length() > 0,
                rx.el.div(
                    rx.foreach(
                        AIAnalysisState.missing_skills, missing_skill_row
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-3",
                ),
                rx.el.p(
                    "Great news — no critical missing skills detected!",
                    class_name="text-sm text-green-700 font-semibold",
                ),
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
        ),
        rx.el.div(
            _list_card(
                "Improvement Suggestions",
                "arrow-up-right",
                AIAnalysisState.improvement_suggestions,
                "No suggestions available.",
                "blue",
            ),
            _list_card(
                "Weaknesses",
                "trending-down",
                AIAnalysisState.weaknesses,
                "No weaknesses listed.",
                "red",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        class_name="flex flex-col gap-6",
    )


def week_card(week: rx.Var, index: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                (index + 1).to_string(),
                class_name="size-9 rounded-full bg-blue-600 text-white text-sm font-bold flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    week["week"],
                    class_name="text-xs font-bold text-blue-600 uppercase tracking-wider",
                ),
                rx.el.p(
                    week["focus"],
                    class_name="text-base font-bold text-gray-900 mt-0.5",
                ),
            ),
            class_name="flex items-center gap-4 mb-4",
        ),
        rx.el.div(
            rx.foreach(
                week["daily_tasks"],
                lambda task, i: rx.el.div(
                    rx.el.div(
                        f"D{i + 1}",
                        class_name="size-7 rounded-lg bg-blue-50 text-blue-700 text-[10px] font-bold flex items-center justify-center shrink-0",
                    ),
                    rx.el.p(
                        task,
                        class_name="text-xs text-gray-700 font-medium leading-relaxed",
                    ),
                    class_name="flex items-start gap-3 p-2.5 rounded-lg hover:bg-slate-50/60 transition-colors",
                ),
            ),
            class_name="flex flex-col gap-1",
        ),
        class_name="p-5 bg-slate-50/40 border border-gray-100 rounded-xl",
    )


def ai_roadmap() -> rx.Component:
    return rx.el.div(
        readiness_hero(),
        rx.el.div(
            rx.el.div(
                rx.icon("calendar-days", class_name="h-4 w-4 text-blue-600"),
                rx.el.h3(
                    "30-Day Daily Roadmap",
                    class_name="text-lg font-bold text-gray-900",
                ),
                class_name="flex items-center gap-2 mb-1",
            ),
            rx.el.p(
                "Personalized week-by-week plan with concrete daily tasks.",
                class_name="text-sm text-gray-500 font-medium mb-6",
            ),
            rx.cond(
                AIAnalysisState.thirty_day_roadmap.length() > 0,
                rx.el.div(
                    rx.foreach(
                        AIAnalysisState.thirty_day_roadmap,
                        lambda w, i: week_card(w, i),
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-4",
                ),
                rx.el.p(
                    "No roadmap generated yet.",
                    class_name="text-sm text-gray-500 font-medium",
                ),
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("folder-git-2", class_name="h-4 w-4 text-blue-600"),
                    rx.el.h3(
                        "Recommended Projects",
                        class_name="text-lg font-bold text-gray-900",
                    ),
                    class_name="flex items-center gap-2 mb-4",
                ),
                rx.el.ul(
                    rx.foreach(
                        AIAnalysisState.recommended_projects,
                        lambda p: rx.el.li(
                            rx.icon(
                                "circle-check",
                                class_name="h-4 w-4 text-blue-600 shrink-0 mt-0.5",
                            ),
                            rx.el.span(
                                p,
                                class_name="text-sm text-gray-700 font-medium leading-relaxed",
                            ),
                            class_name="flex items-start gap-3 py-2",
                        ),
                    ),
                    class_name="flex flex-col divide-y divide-gray-50",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "graduation-cap", class_name="h-4 w-4 text-blue-600"
                    ),
                    rx.el.h3(
                        "Recommended Courses",
                        class_name="text-lg font-bold text-gray-900",
                    ),
                    class_name="flex items-center gap-2 mb-4",
                ),
                rx.el.div(
                    rx.foreach(
                        AIAnalysisState.recommended_courses,
                        lambda c: rx.el.a(
                            rx.el.div(
                                rx.el.p(
                                    c["title"],
                                    class_name="text-sm font-bold text-gray-900",
                                ),
                                rx.el.p(
                                    c["provider"],
                                    class_name="text-xs text-gray-500 font-medium mt-0.5",
                                ),
                            ),
                            rx.icon(
                                "external-link",
                                class_name="h-4 w-4 text-gray-400",
                            ),
                            href=c["url"],
                            is_external=True,
                            class_name="flex items-center justify-between p-3 rounded-xl border border-gray-100 hover:border-blue-300 hover:bg-blue-50/30 transition-colors",
                        ),
                    ),
                    class_name="flex flex-col gap-2",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        rx.el.div(
            _pill_card(
                "Certifications to Pursue",
                "award",
                AIAnalysisState.certifications,
                "No certifications suggested.",
                "blue",
            ),
            _pill_card(
                "Interview Prep Topics",
                "message-circle-question",
                AIAnalysisState.interview_topics,
                "No interview topics generated.",
                "purple",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        class_name="flex flex-col gap-6",
    )


def ai_dashboard_summary() -> rx.Component:
    return rx.el.div(
        readiness_hero(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("check", class_name="h-5 w-5 text-green-600"),
                    class_name="size-10 rounded-xl bg-green-50 flex items-center justify-center mb-4",
                ),
                rx.el.p(
                    AIAnalysisState.existing_skills.length().to_string(),
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "EXISTING SKILLS",
                    class_name="text-xs text-gray-500 font-semibold uppercase tracking-wider mt-1",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("circle-alert", class_name="h-5 w-5 text-red-600"),
                    class_name="size-10 rounded-xl bg-red-50 flex items-center justify-center mb-4",
                ),
                rx.el.p(
                    AIAnalysisState.missing_skills.length().to_string(),
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "MISSING SKILLS",
                    class_name="text-xs text-gray-500 font-semibold uppercase tracking-wider mt-1",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "calendar-days", class_name="h-5 w-5 text-blue-600"
                    ),
                    class_name="size-10 rounded-xl bg-blue-50 flex items-center justify-center mb-4",
                ),
                rx.el.p(
                    AIAnalysisState.thirty_day_roadmap.length().to_string(),
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "ROADMAP WEEKS",
                    class_name="text-xs text-gray-500 font-semibold uppercase tracking-wider mt-1",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("award", class_name="h-5 w-5 text-purple-600"),
                    class_name="size-10 rounded-xl bg-purple-50 flex items-center justify-center mb-4",
                ),
                rx.el.p(
                    AIAnalysisState.certifications.length().to_string(),
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "CERTIFICATIONS",
                    class_name="text-xs text-gray-500 font-semibold uppercase tracking-wider mt-1",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
            ),
            class_name="grid grid-cols-2 lg:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("lightbulb", class_name="h-4 w-4 text-blue-600"),
                rx.el.h3(
                    "Final Career Advice",
                    class_name="text-lg font-bold text-gray-900",
                ),
                class_name="flex items-center gap-2 mb-3",
            ),
            rx.el.p(
                AIAnalysisState.final_career_advice,
                class_name="text-sm text-gray-700 font-medium leading-relaxed",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
        ),
        class_name="flex flex-col gap-6",
    )


def ai_section(
    content_when_ready: rx.Component, cta_label: str
) -> rx.Component:
    return rx.cond(
        AIAnalysisState.is_analyzing,
        loading_card(),
        rx.cond(
            AIAnalysisState.has_analysis,
            rx.el.div(
                content_when_ready,
                error_banner(),
                class_name="flex flex-col gap-6",
            ),
            analysis_cta_panel(cta_label),
        ),
    )

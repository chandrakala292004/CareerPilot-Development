import reflex as rx
from app.components.navigation import navigation
from app.components.footer import footer
from app.components.dashboard_layout import dashboard_layout
from app.components.role_selector import role_selector
from app.components.upload_zone import upload_zone
from app.components.ai_components import (
    ai_section,
    ai_dashboard_summary,
    ai_resume_analysis,
    ai_skill_gap,
    ai_roadmap,
)
from app.states.career import CareerState


def index() -> rx.Component:
    return rx.el.main(
        navigation(),
        # Hero Section
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Autonomously Audited, Precisely Targeted",
                        class_name="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold border border-blue-100 mb-6",
                    ),
                    rx.el.h1(
                        "Navigate Your Next Career Transition with Certainty",
                        class_name="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 tracking-tight leading-none mb-6",
                    ),
                    rx.el.p(
                        "Upload your resume, pinpoint exact target roles, and watch CareerPilot AI autonomously dissect your profile to map out skill gaps, courses, and localized action items.",
                        class_name="text-lg sm:text-xl text-gray-600 max-w-3xl mx-auto font-medium mb-10 leading-relaxed",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Get Started Instantly",
                            href="/dashboard",
                            class_name="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-4 rounded-2xl shadow-sm hover:shadow-lg hover:scale-[1.02] transition-all duration-200",
                        ),
                        rx.el.a(
                            "How it Works",
                            href="/about",
                            class_name="inline-flex items-center gap-2 bg-white hover:bg-gray-50 text-gray-700 font-semibold px-8 py-4 rounded-2xl border border-gray-200 shadow-xs hover:border-gray-300 transition-all duration-200",
                        ),
                        class_name="flex flex-col sm:flex-row justify-center items-center gap-4",
                    ),
                    class_name="text-center",
                ),
                class_name="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-28",
            ),
            class_name="relative overflow-hidden bg-gradient-to-b from-blue-50/40 via-white to-white",
        ),
        # Value Proposition Grid
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Architected for Real Career Progress",
                        class_name="text-2xl sm:text-3xl font-bold text-gray-900 tracking-tight mb-4",
                    ),
                    rx.el.p(
                        "Stop guessing what hiring managers want. Our career engine translates resume signals into quantifiable gaps and step-by-step masterclasses.",
                        class_name="text-base text-gray-500 font-medium max-w-2xl mx-auto",
                    ),
                    class_name="text-center mb-16",
                ),
                rx.el.div(
                    # Card 1
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "shield-alert",
                                class_name="h-6 w-6 text-blue-600",
                            ),
                            class_name="size-12 rounded-xl bg-blue-50 flex items-center justify-center mb-6",
                        ),
                        rx.el.h3(
                            "Automated Gap Auditing",
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "Sifts through text constraints, certifications, and technical definitions to spot crucial knowledge loopholes.",
                            class_name="text-gray-500 font-medium text-sm leading-relaxed",
                        ),
                        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-xs flex flex-col items-start",
                    ),
                    # Card 2
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "target", class_name="h-6 w-6 text-blue-600"
                            ),
                            class_name="size-12 rounded-xl bg-blue-50 flex items-center justify-center mb-6",
                        ),
                        rx.el.h3(
                            "High-Fidelity Targeting",
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "Tailors response algorithms mapped directly to tech leaders like AI Engineer, Data Scientist, or Backend Specialist.",
                            class_name="text-gray-500 font-medium text-sm leading-relaxed",
                        ),
                        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-xs flex flex-col items-start",
                    ),
                    # Card 3
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "trending-up",
                                class_name="h-6 w-6 text-blue-600",
                            ),
                            class_name="size-12 rounded-xl bg-blue-50 flex items-center justify-center mb-6",
                        ),
                        rx.el.h3(
                            "Milestone Pathway",
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "No vague tips. Get concrete recommended code projects, reliable courses, and sequential 30-day schedules.",
                            class_name="text-gray-500 font-medium text-sm leading-relaxed",
                        ),
                        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-xs flex flex-col items-start",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            ),
            id="features",
            class_name="bg-white border-y border-gray-50",
        ),
        # How It Works Flow
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "The Intelligence Loop",
                        class_name="text-2xl sm:text-3xl font-bold text-gray-900 tracking-tight mb-4",
                    ),
                    rx.el.p(
                        "An autonomous cycle that turns resume details into a personalized transition plan.",
                        class_name="text-base text-gray-500 font-medium max-w-2xl mx-auto",
                    ),
                    class_name="text-center mb-16",
                ),
                rx.el.div(
                    # Step 1
                    rx.el.div(
                        rx.el.div(
                            "1",
                            class_name="text-xl font-bold text-blue-600 bg-blue-50 size-10 rounded-full flex items-center justify-center mb-4",
                        ),
                        rx.el.h3(
                            "Profile Assessment",
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "Upload your document. Our parser breaks down skills, project history, and experience markers.",
                            class_name="text-sm text-gray-500 font-medium",
                        ),
                        class_name="relative flex flex-col items-center text-center p-6",
                    ),
                    # Step 2
                    rx.el.div(
                        rx.el.div(
                            "2",
                            class_name="text-xl font-bold text-blue-600 bg-blue-50 size-10 rounded-full flex items-center justify-center mb-4",
                        ),
                        rx.el.h3(
                            "Target Calibration",
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "Choose your target discipline. The system pulls critical real-world requirements from current job structures.",
                            class_name="text-sm text-gray-500 font-medium",
                        ),
                        class_name="relative flex flex-col items-center text-center p-6",
                    ),
                    # Step 3
                    rx.el.div(
                        rx.el.div(
                            "3",
                            class_name="text-xl font-bold text-blue-600 bg-blue-50 size-10 rounded-full flex items-center justify-center mb-4",
                        ),
                        rx.el.h3(
                            "Roadmap Dissemination",
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "Receive an audited score, missing technical modules, recommended code exercises, and study outlines.",
                            class_name="text-sm text-gray-500 font-medium",
                        ),
                        class_name="relative flex flex-col items-center text-center p-6",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8 relative",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
            ),
            id="how-it-works",
            class_name="bg-slate-50/50",
        ),
        # CTA Banner
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Empower Your Transition Journey Now",
                        class_name="text-3xl font-extrabold text-white tracking-tight mb-4",
                    ),
                    rx.el.p(
                        "Start extracting true value from your potential. Stop relying on guessing games and leverage precise, reliable career engineering.",
                        class_name="text-blue-100 text-lg max-w-2xl mx-auto font-medium mb-8",
                    ),
                    rx.el.a(
                        "Access Dashboard",
                        href="/dashboard",
                        class_name="inline-flex items-center gap-2 bg-white hover:bg-blue-50 text-blue-700 font-semibold px-8 py-4 rounded-xl transition-colors duration-200 shadow-sm",
                    ),
                    class_name="text-center max-w-4xl mx-auto",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            ),
            class_name="bg-blue-600",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col justify-between",
    )


def about() -> rx.Component:
    return rx.el.main(
        navigation(),
        rx.el.div(
            rx.el.div(
                # Header block
                rx.el.div(
                    rx.el.span(
                        "Autonomous Platform Intel",
                        class_name="inline-flex items-center px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold border border-blue-100 mb-4",
                    ),
                    rx.el.h1(
                        "Behind the CareerPilot Engine",
                        class_name="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight mb-4",
                    ),
                    rx.el.p(
                        "A strict look into how our platform parses skills, respects developer privacy, and maps roles.",
                        class_name="text-base text-gray-500 font-medium max-w-2xl mx-auto",
                    ),
                    class_name="text-center mb-16",
                ),
                # Content Grid
                rx.el.div(
                    # Left column: Tech Stack & Workflow
                    rx.el.div(
                        rx.el.h2(
                            "Platform & Pipeline Architecture",
                            class_name="text-xl font-bold text-gray-900 mb-6 flex items-center gap-2",
                        ),
                        rx.el.p(
                            "CareerPilot AI relies on high-fidelity parsed semantic analysis to understand the capabilities embedded in standard CV structures. We target several key areas to build optimized recommendations:",
                            class_name="text-sm text-gray-600 font-medium mb-4 leading-relaxed",
                        ),
                        rx.el.ul(
                            rx.el.li(
                                rx.el.strong(
                                    "Technical Core Index: ",
                                    class_name="text-gray-900 font-semibold",
                                ),
                                "Maps frameworks, languages, APIs, databases, and architectural concepts.",
                                class_name="text-sm text-gray-500 font-medium mb-3",
                            ),
                            rx.el.li(
                                rx.el.strong(
                                    "Cross-Discipline Alignment: ",
                                    class_name="text-gray-900 font-semibold",
                                ),
                                "Weights matching priorities against target roles (e.g., verifying if a candidate possesses Python-centric system knowledge vs. analytical model training).",
                                class_name="text-sm text-gray-500 font-medium mb-3",
                            ),
                            rx.el.li(
                                rx.el.strong(
                                    "Resource Dispatcher: ",
                                    class_name="text-gray-900 font-semibold",
                                ),
                                "Queries optimized public catalogs to recommend real-world project directions, concrete certifications, and specific technical milestones.",
                                class_name="text-sm text-gray-500 font-medium",
                            ),
                            class_name="list-disc pl-5 mb-8",
                        ),
                        rx.el.h2(
                            "Covered Disciplines",
                            class_name="text-xl font-bold text-gray-900 mb-6",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "AI Engineer",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Data Analyst",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Data Scientist",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Full Stack Developer",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Frontend Developer",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Backend Developer",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Java Developer",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            rx.el.span(
                                "Python Developer",
                                class_name="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-lg border border-blue-100",
                            ),
                            class_name="flex flex-wrap gap-2.5",
                        ),
                        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-xs",
                    ),
                    # Right column: Privacy & Standards
                    rx.el.div(
                        rx.el.h2(
                            "Privacy & Ethical Operations",
                            class_name="text-xl font-bold text-gray-900 mb-6",
                        ),
                        rx.el.p(
                            "We operate under strict zero-retention principles. Your document and extracted context are isolated during analysis and are not used for public model training.",
                            class_name="text-sm text-gray-600 font-medium mb-6 leading-relaxed",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "lock",
                                    class_name="h-5 w-5 text-blue-600 shrink-0",
                                ),
                                rx.el.div(
                                    rx.el.h4(
                                        "No Persistent Storage",
                                        class_name="text-sm font-bold text-gray-900 mb-1",
                                    ),
                                    rx.el.p(
                                        "Resumes uploaded are processed in-memory. We do not store raw resume records indefinitely on database models.",
                                        class_name="text-xs text-gray-500 font-medium",
                                    ),
                                ),
                                class_name="flex gap-4 mb-6",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "eye-off",
                                    class_name="h-5 w-5 text-blue-600 shrink-0",
                                ),
                                rx.el.div(
                                    rx.el.h4(
                                        "Anonymized Metadata",
                                        class_name="text-sm font-bold text-gray-900 mb-1",
                                    ),
                                    rx.el.p(
                                        "Personally Identifiable Information (PII) like home addresses or phone numbers is skipped during our core pipeline execution.",
                                        class_name="text-xs text-gray-500 font-medium",
                                    ),
                                ),
                                class_name="flex gap-4 mb-6",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "file-check",
                                    class_name="h-5 w-5 text-blue-600 shrink-0",
                                ),
                                rx.el.div(
                                    rx.el.h4(
                                        "ATS Optimization Ready",
                                        class_name="text-sm font-bold text-gray-900 mb-1",
                                    ),
                                    rx.el.p(
                                        "Your advice outlines format enhancements ensuring modern Application Tracking Systems (ATS) index your document flawlessly.",
                                        class_name="text-xs text-gray-500 font-medium",
                                    ),
                                ),
                                class_name="flex gap-4",
                            ),
                        ),
                        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-xs flex flex-col justify-between",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            ),
            class_name="bg-slate-50/40",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col justify-between",
    )


def _page_header(title: str, subtitle: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name="h-5 w-5 text-blue-600"),
                class_name="size-10 rounded-xl bg-blue-50 flex items-center justify-center",
            ),
            rx.el.div(
                rx.el.h1(
                    title,
                    class_name="text-2xl sm:text-3xl font-bold text-gray-900 tracking-tight",
                ),
                rx.el.p(
                    subtitle,
                    class_name="text-sm text-gray-500 font-medium mt-1",
                ),
            ),
            class_name="flex items-start gap-4",
        ),
        class_name="mb-8",
    )


def _readiness_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Career Readiness",
                    class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider",
                ),
                rx.el.div(
                    rx.el.span(
                        CareerState.readiness_score.to_string(),
                        class_name="text-5xl font-extrabold text-gray-900 tracking-tight",
                    ),
                    rx.el.span(
                        "%", class_name="text-2xl font-bold text-gray-400 ml-1"
                    ),
                    class_name="mt-2",
                ),
                rx.el.p(
                    CareerState.readiness_label,
                    class_name="text-sm font-semibold text-blue-700 mt-1",
                ),
            ),
            rx.el.div(
                rx.icon("gauge", class_name="h-6 w-6 text-blue-600"),
                class_name="size-12 rounded-xl bg-blue-50 flex items-center justify-center",
            ),
            class_name="flex justify-between items-start",
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-2 bg-blue-500 rounded-full transition-all",
                style={"width": f"{CareerState.readiness_score}%"},
            ),
            class_name="w-full h-2 bg-gray-100 rounded-full overflow-hidden mt-6",
        ),
        rx.el.p(
            rx.cond(
                CareerState.has_resume,
                f"Based on {CareerState.matched_skills.length()} of {CareerState.role['core_skills'].length()} core {CareerState.role['name']} skills detected.",
                "Upload a resume to compute your readiness score.",
            ),
            class_name="text-xs text-gray-500 font-medium mt-3",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
    )


def _stat_card(label: str, value, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-5 w-5 text-{color}-600"),
            class_name=f"size-10 rounded-xl bg-{color}-50 flex items-center justify-center mb-4",
        ),
        rx.el.p(value, class_name="text-2xl font-bold text-gray-900"),
        rx.el.p(
            label,
            class_name="text-xs text-gray-500 font-semibold uppercase tracking-wider mt-1",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
    )


def _skill_pill(skill: str, matched: bool) -> rx.Component:
    return rx.el.span(
        rx.icon(
            rx.cond(matched, "check", "circle-dashed"),
            class_name="h-3 w-3",
        ),
        skill,
        class_name=rx.cond(
            matched,
            "inline-flex items-center gap-1.5 px-2.5 py-1 bg-green-50 text-green-700 text-xs font-semibold rounded-lg border border-green-100",
            "inline-flex items-center gap-1.5 px-2.5 py-1 bg-red-50 text-red-700 text-xs font-semibold rounded-lg border border-red-100",
        ),
    )


def _no_resume_prompt() -> rx.Component:
    return rx.el.div(
        rx.icon("file-question", class_name="h-10 w-10 text-gray-300 mb-3"),
        rx.el.h4(
            "Upload a resume to unlock this view",
            class_name="text-base font-bold text-gray-800 mb-1",
        ),
        rx.el.p(
            "Return to the dashboard, upload your resume, and choose a target role.",
            class_name="text-sm text-gray-500 font-medium mb-4",
        ),
        rx.el.a(
            "Go to Dashboard",
            href="/dashboard",
            class_name="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-4 py-2 rounded-xl transition-colors",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-xs flex flex-col items-center justify-center text-center",
    )


def dashboard_page() -> rx.Component:
    return dashboard_layout(
        _page_header(
            "Career Intelligence Dashboard",
            "Configure your target role, upload your resume, and generate an AI-powered readiness report.",
            "layout-dashboard",
        ),
        _stale_analysis_banner(),
        rx.el.div(
            rx.el.div(
                role_selector(),
                upload_zone(),
                class_name="flex flex-col gap-6",
            ),
            rx.el.div(
                _readiness_card(),
                rx.el.div(
                    _stat_card(
                        "Matched Skills",
                        CareerState.matched_skills.length().to_string(),
                        "circle-check",
                        "green",
                    ),
                    _stat_card(
                        "Missing Skills",
                        CareerState.missing_skills.length().to_string(),
                        "circle-alert",
                        "red",
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Quick Navigation",
                        class_name="text-lg font-bold text-gray-900 mb-4",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "file-text", class_name="h-4 w-4 text-blue-600"
                            ),
                            rx.el.span(
                                "Resume Analysis",
                                class_name="text-sm font-semibold text-gray-900",
                            ),
                            rx.icon(
                                "chevron-right",
                                class_name="h-4 w-4 text-gray-400 ml-auto",
                            ),
                            href="/dashboard/resume",
                            class_name="flex items-center gap-3 px-4 py-3 rounded-xl border border-gray-100 hover:border-blue-300 hover:bg-blue-50/30 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon(
                                "target", class_name="h-4 w-4 text-blue-600"
                            ),
                            rx.el.span(
                                "Skill Gap Analysis",
                                class_name="text-sm font-semibold text-gray-900",
                            ),
                            rx.icon(
                                "chevron-right",
                                class_name="h-4 w-4 text-gray-400 ml-auto",
                            ),
                            href="/dashboard/skill-gap",
                            class_name="flex items-center gap-3 px-4 py-3 rounded-xl border border-gray-100 hover:border-blue-300 hover:bg-blue-50/30 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("map", class_name="h-4 w-4 text-blue-600"),
                            rx.el.span(
                                "AI Career Roadmap",
                                class_name="text-sm font-semibold text-gray-900",
                            ),
                            rx.icon(
                                "chevron-right",
                                class_name="h-4 w-4 text-gray-400 ml-auto",
                            ),
                            href="/dashboard/roadmap",
                            class_name="flex items-center gap-3 px-4 py-3 rounded-xl border border-gray-100 hover:border-blue-300 hover:bg-blue-50/30 transition-colors",
                        ),
                        class_name="flex flex-col gap-2",
                    ),
                    class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
                ),
                class_name="flex flex-col gap-6",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("sparkles", class_name="h-5 w-5 text-blue-600"),
                    rx.el.h2(
                        "AI Career Intelligence",
                        class_name="text-xl font-bold text-gray-900",
                    ),
                    class_name="flex items-center gap-2 mb-2",
                ),
                rx.el.p(
                    "Powered by Gemini 2.5 Flash. Get a personalized readiness score, skill-gap breakdown, ATS tips, and a 30-day roadmap.",
                    class_name="text-sm text-gray-500 font-medium",
                ),
                class_name="mb-6",
            ),
            ai_section(ai_dashboard_summary(), "Generate AI Career Report"),
        ),
    )


def resume_analysis_page() -> rx.Component:
    return dashboard_layout(
        _page_header(
            "Resume Analysis",
            "Extracted content from your resume with role-aware skill signals.",
            "file-text",
        ),
        _stale_analysis_banner(),
        rx.cond(
            CareerState.has_resume,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "File",
                                class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                CareerState.resume_filename,
                                class_name="text-sm font-bold text-gray-900 mt-1 truncate",
                            ),
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Words",
                                class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                CareerState.resume_word_count.to_string(),
                                class_name="text-sm font-bold text-gray-900 mt-1",
                            ),
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Characters",
                                class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                CareerState.resume_char_count.to_string(),
                                class_name="text-sm font-bold text-gray-900 mt-1",
                            ),
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Detected Skills",
                                class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                CareerState.detected_skills.length().to_string(),
                                class_name="text-sm font-bold text-gray-900 mt-1",
                            ),
                        ),
                        class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
                    ),
                    class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Detected Skills (Keyword Scan)",
                            class_name="text-lg font-bold text-gray-900 mb-4",
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
                                "No known skills detected via keyword scan.",
                                class_name="text-sm text-gray-500 font-medium",
                            ),
                        ),
                    ),
                    class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Extracted Text",
                            class_name="text-lg font-bold text-gray-900",
                        ),
                        rx.el.p(
                            "This is exactly what the AI engine will see.",
                            class_name="text-xs text-gray-500 font-medium mt-1",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.pre(
                        rx.el.code(CareerState.resume_text),
                        class_name="text-xs text-gray-700 font-mono whitespace-pre-wrap bg-slate-50/60 p-4 rounded-xl border border-gray-100 max-h-96 overflow-auto",
                    ),
                    class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("sparkles", class_name="h-5 w-5 text-blue-600"),
                        rx.el.h2(
                            "AI Resume Analysis",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        class_name="flex items-center gap-2 mb-6",
                    ),
                    ai_section(
                        ai_resume_analysis(), "Run Deep Resume Analysis"
                    ),
                ),
            ),
            _no_resume_prompt(),
        ),
    )


def skill_gap_page() -> rx.Component:
    return dashboard_layout(
        _page_header(
            "Skill Gap Analysis",
            "Compare your detected skills against your target role's core requirements.",
            "target",
        ),
        _stale_analysis_banner(),
        rx.cond(
            CareerState.has_resume,
            rx.el.div(
                rx.el.div(
                    _readiness_card(),
                    _stat_card(
                        "Matched",
                        CareerState.matched_skills.length().to_string(),
                        "circle-check",
                        "green",
                    ),
                    _stat_card(
                        "Missing",
                        CareerState.missing_skills.length().to_string(),
                        "circle-alert",
                        "red",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "circle-check",
                                class_name="h-4 w-4 text-green-600",
                            ),
                            rx.el.h3(
                                "Skills You Have",
                                class_name="text-lg font-bold text-gray-900",
                            ),
                            class_name="flex items-center gap-2 mb-4",
                        ),
                        rx.cond(
                            CareerState.matched_skills.length() > 0,
                            rx.el.div(
                                rx.foreach(
                                    CareerState.matched_skills,
                                    lambda s: _skill_pill(s, True),
                                ),
                                class_name="flex flex-wrap gap-1.5",
                            ),
                            rx.el.p(
                                "None of the target role's core skills were detected.",
                                class_name="text-sm text-gray-500 font-medium",
                            ),
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "circle-alert",
                                class_name="h-4 w-4 text-red-600",
                            ),
                            rx.el.h3(
                                "Skills to Learn",
                                class_name="text-lg font-bold text-gray-900",
                            ),
                            class_name="flex items-center gap-2 mb-4",
                        ),
                        rx.cond(
                            CareerState.missing_skills.length() > 0,
                            rx.el.div(
                                rx.foreach(
                                    CareerState.missing_skills,
                                    lambda s: _skill_pill(s, False),
                                ),
                                class_name="flex flex-wrap gap-1.5",
                            ),
                            rx.el.p(
                                "You cover all core skills. Time to focus on projects and depth.",
                                class_name="text-sm text-green-700 font-semibold",
                            ),
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Recommended Tools to Master",
                            class_name="text-lg font-bold text-gray-900 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                CareerState.role["tools"],
                                lambda t: rx.el.span(
                                    t,
                                    class_name="px-3 py-1.5 bg-slate-50 text-gray-700 text-xs font-semibold rounded-lg border border-gray-200",
                                ),
                            ),
                            class_name="flex flex-wrap gap-2",
                        ),
                    ),
                    class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("sparkles", class_name="h-5 w-5 text-blue-600"),
                        rx.el.h2(
                            "AI Skill Gap Report",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        class_name="flex items-center gap-2 mb-6",
                    ),
                    ai_section(ai_skill_gap(), "Generate AI Skill Gap Report"),
                ),
            ),
            _no_resume_prompt(),
        ),
    )


def _stale_analysis_banner() -> rx.Component:
    from app.states.ai_analysis import AIAnalysisState

    is_stale = AIAnalysisState.has_analysis & (
        AIAnalysisState.analyzed_role_id != CareerState.selected_role_id
    )
    return rx.cond(
        is_stale,
        rx.el.div(
            rx.icon(
                "info", class_name="h-5 w-5 text-amber-600 shrink-0 mt-0.5"
            ),
            rx.el.div(
                rx.el.p(
                    "Your target role changed",
                    class_name="text-sm font-bold text-amber-800",
                ),
                rx.el.p(
                    f"Current AI analysis was generated for '{AIAnalysisState.analyzed_role_name}'. Re-run analysis to refresh results for '{CareerState.role['name']}'.",
                    class_name="text-xs text-amber-700 font-medium mt-0.5",
                ),
            ),
            class_name="flex items-start gap-3 p-4 bg-amber-50 border border-amber-100 rounded-2xl mb-6",
        ),
        rx.fragment(),
    )


def roadmap_page() -> rx.Component:
    return dashboard_layout(
        _page_header(
            "AI Career Roadmap",
            f"Your 30-day plan to become a {CareerState.role['name']}.",
            "map",
        ),
        _stale_analysis_banner(),
        rx.cond(
            CareerState.has_resume,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "30-Day Weekly Plan",
                            class_name="text-lg font-bold text-gray-900 mb-1",
                        ),
                        rx.el.p(
                            "Curated milestones based on your target role.",
                            class_name="text-sm text-gray-500 font-medium mb-6",
                        ),
                        rx.el.div(
                            rx.foreach(
                                CareerState.role["roadmap"],
                                lambda item, i: rx.el.div(
                                    rx.el.div(
                                        rx.el.div(
                                            (i + 1).to_string(),
                                            class_name="size-8 rounded-full bg-blue-600 text-white text-sm font-bold flex items-center justify-center shrink-0",
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                item["week"],
                                                class_name="text-xs font-bold text-blue-600 uppercase tracking-wider",
                                            ),
                                            rx.el.p(
                                                item["focus"],
                                                class_name="text-base font-bold text-gray-900 mt-0.5",
                                            ),
                                            rx.el.p(
                                                item["tasks"],
                                                class_name="text-sm text-gray-600 font-medium mt-2 leading-relaxed",
                                            ),
                                        ),
                                        class_name="flex gap-4",
                                    ),
                                    class_name="p-5 bg-slate-50/40 border border-gray-100 rounded-xl",
                                ),
                            ),
                            class_name="flex flex-col gap-3",
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "folder-git-2",
                                class_name="h-4 w-4 text-blue-600",
                            ),
                            rx.el.h3(
                                "Recommended Projects",
                                class_name="text-lg font-bold text-gray-900",
                            ),
                            class_name="flex items-center gap-2 mb-4",
                        ),
                        rx.el.ul(
                            rx.foreach(
                                CareerState.role["projects"],
                                lambda p: rx.el.li(
                                    rx.icon(
                                        "circle-check",
                                        class_name="h-4 w-4 text-blue-600 shrink-0 mt-0.5",
                                    ),
                                    rx.el.span(
                                        p,
                                        class_name="text-sm text-gray-700 font-medium",
                                    ),
                                    class_name="flex items-start gap-3 p-3 rounded-xl hover:bg-slate-50/60 transition-colors",
                                ),
                            ),
                            class_name="flex flex-col gap-1",
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-xs",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "graduation-cap",
                                class_name="h-4 w-4 text-blue-600",
                            ),
                            rx.el.h3(
                                "Recommended Courses",
                                class_name="text-lg font-bold text-gray-900",
                            ),
                            class_name="flex items-center gap-2 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                CareerState.role["courses"],
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
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("sparkles", class_name="h-5 w-5 text-blue-600"),
                        rx.el.h2(
                            "Personalized AI Roadmap",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        class_name="flex items-center gap-2 mb-6",
                    ),
                    ai_section(
                        ai_roadmap(), "Generate Personalized AI Roadmap"
                    ),
                ),
            ),
            _no_resume_prompt(),
        ),
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(resume_analysis_page, route="/dashboard/resume")
app.add_page(skill_gap_page, route="/dashboard/skill-gap")
app.add_page(roadmap_page, route="/dashboard/roadmap")

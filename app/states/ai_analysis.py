import reflex as rx
import os
import json
import logging
import re
import asyncio
from typing import TypedDict


class MissingSkillItem(TypedDict):
    skill: str
    importance: str
    estimated_learning_time: str


class CourseItem(TypedDict):
    title: str
    provider: str
    url: str


class RoadmapWeekItem(TypedDict):
    week: str
    focus: str
    daily_tasks: list[str]


PROMPT_TEMPLATE = """You are a senior technical recruiter and career coach. Analyze the resume against the target role and return concise, actionable JSON.

Target Role: {role_name}
Core Skills Reference: {role_skills}
Tools Reference: {role_tools}

Resume:
\"\"\"
{resume_text}
\"\"\"

Return ONLY a JSON object with these exact keys:
- career_readiness_score: int 0-100
- score_explanation: string (2 sentences)
- existing_skills: string[] (skills present in resume)
- technical_skills: string[]
- soft_skills: string[]
- missing_skills: array of {{skill, importance ("High"|"Medium"|"Low"), estimated_learning_time}} (4-8 items)
- strengths: string[] (3-5)
- weaknesses: string[] (3-5)
- recommended_courses: array of {{title, provider, url}} (3-5)
- recommended_projects: string[] (4-6)
- thirty_day_roadmap: array of EXACTLY 4 objects {{week, focus, daily_tasks: string[7]}} (Week 1-4, 7 short daily tasks each)
- certifications: string[] (3-5)
- interview_topics: string[] (5-8)
- ats_tips: string[] (4-5)
- improvement_suggestions: string[] (4-5)
- final_career_advice: string (2-3 sentences)

Rules: keep each string under 140 chars. Base judgments on actual resume content. Return only JSON, no markdown, no prose.
"""


def _strip_json_fences(text: str) -> str:
    text = text.strip()
    if text.startswith(""):
        text = re.sub(r"^(?:json)?\s*", "", text)
        text = re.sub(r"\s*$", "", text)
    return text.strip()


def _safe_parse_json(text: str) -> dict:
    cleaned = _strip_json_fences(text)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        logging.exception("Unexpected error")
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise


class AIAnalysisState(rx.State):
    is_analyzing: bool = False
    analysis_error: str = ""
    has_analysis: bool = False
    analyzed_role_id: str = ""
    analyzed_role_name: str = ""

    career_readiness_score: int = 0
    score_explanation: str = ""
    existing_skills: list[str] = []
    technical_skills: list[str] = []
    soft_skills: list[str] = []
    missing_skills: list[MissingSkillItem] = []
    strengths: list[str] = []
    weaknesses: list[str] = []
    recommended_courses: list[CourseItem] = []
    recommended_projects: list[str] = []
    thirty_day_roadmap: list[RoadmapWeekItem] = []
    certifications: list[str] = []
    interview_topics: list[str] = []
    ats_tips: list[str] = []
    improvement_suggestions: list[str] = []
    final_career_advice: str = ""

    @rx.var
    def readiness_label(self) -> str:
        s = self.career_readiness_score
        if s == 0:
            return "Not Assessed"
        if s < 35:
            return "Early Stage"
        if s < 60:
            return "Developing"
        if s < 80:
            return "Interview Ready"
        return "Strong Match"

    @rx.event
    def clear_analysis(self):
        self.has_analysis = False
        self.analysis_error = ""
        self.career_readiness_score = 0
        self.score_explanation = ""
        self.existing_skills = []
        self.technical_skills = []
        self.soft_skills = []
        self.missing_skills = []
        self.strengths = []
        self.weaknesses = []
        self.recommended_courses = []
        self.recommended_projects = []
        self.thirty_day_roadmap = []
        self.certifications = []
        self.interview_topics = []
        self.ats_tips = []
        self.improvement_suggestions = []
        self.final_career_advice = ""

    @rx.event(background=True)
    async def run_analysis(self):
        from app.states.career import CareerState

        async with self:
            career = await self.get_state(CareerState)
            resume_text = career.resume_text
            role_name = career.role["name"]
            role_id = career.role["id"]
            role_skills = ", ".join(career.role["core_skills"])
            role_tools = ", ".join(career.role["tools"])

            if not resume_text or len(resume_text) < 50:
                self.analysis_error = "Please upload a resume with at least 50 characters of readable content."
                return
            if self.is_analyzing:
                return

            self.is_analyzing = True
            self.analysis_error = ""

        api_key = os.getenv("GOOGLE_API_KEY", "").strip()
        if not api_key:
            async with self:
                self.is_analyzing = False
                self.analysis_error = (
                    "AI analysis is unavailable: the GOOGLE_API_KEY environment "
                    "variable is not configured on this deployment. Set it in your "
                    "environment (e.g. in a .env file or hosting dashboard) and "
                    "restart the app to enable Gemini-powered analysis."
                )
            return

        # Trim resume to a safe context window to keep the request fast and bounded.
        trimmed_resume = resume_text[:6000]
        prompt = PROMPT_TEMPLATE.format(
            role_name=role_name,
            role_skills=role_skills,
            role_tools=role_tools,
            resume_text=trimmed_resume,
        )

        raw_text = ""
        try:
            from google import genai

            client = genai.Client(api_key=api_key)

            def _call_gemini() -> str:
                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json",
                        "temperature": 0.4,
                        "max_output_tokens": 4096,
                    },
                )
                return response.text or ""

            raw_text = await asyncio.wait_for(
                asyncio.to_thread(_call_gemini), timeout=60.0
            )
        except asyncio.TimeoutError:
            logging.exception("Gemini API call timed out")
            async with self:
                self.is_analyzing = False
                self.analysis_error = (
                    "AI analysis timed out after 60 seconds. Please try again — "
                    "shorter resumes typically complete faster."
                )
            return
        except Exception as e:
            logging.exception(f"Gemini API call failed: {e}")
            async with self:
                self.is_analyzing = False
                self.analysis_error = f"AI analysis request failed: {str(e)[:200]}. Please try again."
            return

        if not raw_text.strip():
            async with self:
                self.is_analyzing = False
                self.analysis_error = (
                    "AI returned an empty response. Please retry the analysis."
                )
            return

        try:
            data = _safe_parse_json(raw_text)
        except Exception as e:
            logging.exception(f"JSON parse failed: {e}")
            async with self:
                self.is_analyzing = False
                self.analysis_error = "The AI returned an unexpected response format. Please retry — this usually resolves on a second attempt."
            return

        try:
            required_fields = [
                "career_readiness_score",
                "existing_skills",
                "missing_skills",
                "thirty_day_roadmap",
                "recommended_projects",
            ]
            missing_fields = [f for f in required_fields if f not in data]
            if missing_fields:
                logging.error(f"AI response missing fields: {missing_fields}")
                async with self:
                    self.is_analyzing = False
                    self.analysis_error = (
                        f"AI response was incomplete (missing: {', '.join(missing_fields)}). "
                        "Please retry — this usually resolves on a second attempt."
                    )
                return
        except Exception as e:
            logging.exception(f"Error checking required fields: {e}")
            async with self:
                self.is_analyzing = False
                self.analysis_error = (
                    "Failed to read the structure of the AI analysis response."
                )
            return

        try:
            score_raw = data.get("career_readiness_score", 0)
            try:
                score = int(score_raw)
            except (TypeError, ValueError):
                score = 0
            score = max(0, min(100, score))

            missing_raw = data.get("missing_skills", []) or []
            missing_skills: list[MissingSkillItem] = []
            for item in missing_raw:
                if isinstance(item, dict):
                    missing_skills.append(
                        MissingSkillItem(
                            skill=str(item.get("skill", "")).strip(),
                            importance=str(item.get("importance", "Medium"))
                            .strip()
                            .title(),
                            estimated_learning_time=str(
                                item.get("estimated_learning_time", "")
                            ).strip(),
                        )
                    )
                elif isinstance(item, str):
                    missing_skills.append(
                        MissingSkillItem(
                            skill=item,
                            importance="Medium",
                            estimated_learning_time="",
                        )
                    )

            courses_raw = data.get("recommended_courses", []) or []
            courses: list[CourseItem] = []
            for c in courses_raw:
                if isinstance(c, dict):
                    courses.append(
                        CourseItem(
                            title=str(c.get("title", "")).strip(),
                            provider=str(c.get("provider", "")).strip(),
                            url=str(c.get("url", "")).strip(),
                        )
                    )

            roadmap_raw = data.get("thirty_day_roadmap", []) or []
            roadmap: list[RoadmapWeekItem] = []
            for w in roadmap_raw:
                if isinstance(w, dict):
                    tasks = w.get("daily_tasks", []) or []
                    if not isinstance(tasks, list):
                        tasks = []
                    roadmap.append(
                        RoadmapWeekItem(
                            week=str(w.get("week", "")).strip(),
                            focus=str(w.get("focus", "")).strip(),
                            daily_tasks=[str(t) for t in tasks],
                        )
                    )

            def _slist(key: str) -> list[str]:
                v = data.get(key, []) or []
                if not isinstance(v, list):
                    return []
                return [str(x) for x in v if x is not None]

            async with self:
                self.career_readiness_score = score
                self.score_explanation = str(
                    data.get("score_explanation", "")
                ).strip()
                self.existing_skills = _slist("existing_skills")
                self.technical_skills = _slist("technical_skills")
                self.soft_skills = _slist("soft_skills")
                self.missing_skills = missing_skills
                self.strengths = _slist("strengths")
                self.weaknesses = _slist("weaknesses")
                self.recommended_courses = courses
                self.recommended_projects = _slist("recommended_projects")
                self.thirty_day_roadmap = roadmap
                self.certifications = _slist("certifications")
                self.interview_topics = _slist("interview_topics")
                self.ats_tips = _slist("ats_tips")
                self.improvement_suggestions = _slist("improvement_suggestions")
                self.final_career_advice = str(
                    data.get("final_career_advice", "")
                ).strip()
                self.has_analysis = True
                self.analyzed_role_id = role_id
                self.analyzed_role_name = role_name
                self.is_analyzing = False
                self.analysis_error = ""
        except Exception as e:
            logging.exception(f"Failed to process AI response: {e}")
            async with self:
                self.is_analyzing = False
                self.analysis_error = "The AI response was missing expected fields. Please retry the analysis."

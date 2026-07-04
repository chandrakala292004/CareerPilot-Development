import reflex as rx
import io
import logging
from typing import TypedDict


class RoleData(TypedDict):
    id: str
    name: str
    icon: str
    description: str
    core_skills: list[str]
    tools: list[str]
    projects: list[str]
    courses: list[dict[str, str]]
    roadmap: list[dict[str, str]]


ROLES: dict[str, RoleData] = {
    "ai-engineer": {
        "id": "ai-engineer",
        "name": "AI Engineer",
        "icon": "brain-circuit",
        "description": "Design, build and deploy machine learning and generative AI systems into production.",
        "core_skills": [
            "Python",
            "PyTorch",
            "TensorFlow",
            "LLM APIs",
            "Prompt Engineering",
            "Vector Databases",
            "MLOps",
            "Docker",
            "REST APIs",
            "Linear Algebra",
        ],
        "tools": [
            "OpenAI API",
            "LangChain",
            "Hugging Face",
            "Pinecone",
            "AWS SageMaker",
        ],
        "projects": [
            "Build a RAG chatbot using LangChain and a vector DB",
            "Fine-tune a transformer for domain-specific classification",
            "Deploy an ML model behind a FastAPI service with Docker",
            "Create an autonomous multi-tool agent with function calling",
        ],
        "courses": [
            {
                "title": "Deep Learning Specialization",
                "provider": "Coursera",
                "url": "https://www.coursera.org/specializations/deep-learning",
            },
            {
                "title": "LangChain for LLM App Development",
                "provider": "DeepLearning.AI",
                "url": "https://www.deeplearning.ai/short-courses/",
            },
            {
                "title": "Full Stack Deep Learning",
                "provider": "FSDL",
                "url": "https://fullstackdeeplearning.com/",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "Python + ML foundations",
                "tasks": "Refresh NumPy, Pandas, Scikit-learn. Complete two Kaggle intros.",
            },
            {
                "week": "Week 2",
                "focus": "Deep Learning core",
                "tasks": "Study neural nets, backprop, and build an MLP + CNN in PyTorch.",
            },
            {
                "week": "Week 3",
                "focus": "LLMs & GenAI",
                "tasks": "Explore transformer architecture, prompt engineering, RAG concepts.",
            },
            {
                "week": "Week 4",
                "focus": "Production & Deployment",
                "tasks": "Ship a portfolio LLM app with FastAPI, Docker, and CI/CD.",
            },
        ],
    },
    "data-analyst": {
        "id": "data-analyst",
        "name": "Data Analyst",
        "icon": "chart-bar",
        "description": "Turn raw data into actionable insights via SQL, dashboards, and statistical analysis.",
        "core_skills": [
            "SQL",
            "Excel",
            "Python",
            "Pandas",
            "Statistics",
            "Tableau",
            "Power BI",
            "Data Cleaning",
            "A/B Testing",
            "Storytelling",
        ],
        "tools": ["SQL", "Tableau", "Power BI", "Google Sheets", "Looker"],
        "projects": [
            "Build a sales KPI dashboard in Tableau or Power BI",
            "Perform a cohort retention analysis in SQL",
            "Publish an EDA notebook on a public dataset",
            "Design and analyze an A/B test with Python",
        ],
        "courses": [
            {
                "title": "Google Data Analytics Certificate",
                "provider": "Coursera",
                "url": "https://www.coursera.org/professional-certificates/google-data-analytics",
            },
            {
                "title": "SQL for Data Science",
                "provider": "UC Davis / Coursera",
                "url": "https://www.coursera.org/learn/sql-for-data-science",
            },
            {
                "title": "Tableau A-Z",
                "provider": "Udemy",
                "url": "https://www.udemy.com/topic/tableau/",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "SQL fluency",
                "tasks": "Master joins, aggregations, window functions on StrataScratch.",
            },
            {
                "week": "Week 2",
                "focus": "Python + Pandas",
                "tasks": "Clean and explore two real datasets end-to-end.",
            },
            {
                "week": "Week 3",
                "focus": "Visualization",
                "tasks": "Ship two polished Tableau or Power BI dashboards.",
            },
            {
                "week": "Week 4",
                "focus": "Statistics + storytelling",
                "tasks": "Learn hypothesis testing, present analysis with clear narrative.",
            },
        ],
    },
    "data-scientist": {
        "id": "data-scientist",
        "name": "Data Scientist",
        "icon": "flask-conical",
        "description": "Blend statistics, ML, and domain expertise to build predictive models and drive decisions.",
        "core_skills": [
            "Python",
            "R",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Feature Engineering",
            "Deep Learning",
            "Experimentation",
            "Data Visualization",
            "Communication",
        ],
        "tools": ["Jupyter", "Scikit-learn", "XGBoost", "MLflow", "Airflow"],
        "projects": [
            "Predict customer churn with a full ML pipeline",
            "Build a recommender system with collaborative filtering",
            "End-to-end forecasting model with feature store",
            "Deploy a model to production with MLflow",
        ],
        "courses": [
            {
                "title": "IBM Data Science Certificate",
                "provider": "Coursera",
                "url": "https://www.coursera.org/professional-certificates/ibm-data-science",
            },
            {
                "title": "Machine Learning Specialization",
                "provider": "Coursera / Andrew Ng",
                "url": "https://www.coursera.org/specializations/machine-learning-introduction",
            },
            {
                "title": "Practical Statistics for Data Scientists",
                "provider": "O'Reilly",
                "url": "https://www.oreilly.com/",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "Statistics & Python",
                "tasks": "Distributions, hypothesis testing, Pandas mastery.",
            },
            {
                "week": "Week 2",
                "focus": "Classical ML",
                "tasks": "Linear/logistic regression, trees, ensembles on Kaggle.",
            },
            {
                "week": "Week 3",
                "focus": "Deep Learning + NLP",
                "tasks": "Build one CV project and one text classification project.",
            },
            {
                "week": "Week 4",
                "focus": "Deployment",
                "tasks": "Package with MLflow, deploy REST endpoint, write case study.",
            },
        ],
    },
    "full-stack": {
        "id": "full-stack",
        "name": "Full Stack Developer",
        "icon": "layers",
        "description": "Own front-end, back-end, and database work to ship complete web applications.",
        "core_skills": [
            "JavaScript",
            "TypeScript",
            "React",
            "Node.js",
            "REST APIs",
            "SQL",
            "Git",
            "HTML/CSS",
            "Testing",
            "System Design",
        ],
        "tools": ["React", "Next.js", "Node.js", "PostgreSQL", "Docker"],
        "projects": [
            "Build a SaaS starter with auth, billing, and dashboards",
            "Real-time chat with WebSockets and PostgreSQL",
            "Blog platform with Next.js and a headless CMS",
            "Dockerized microservices with a React front-end",
        ],
        "courses": [
            {
                "title": "The Complete Web Developer Bootcamp",
                "provider": "Udemy",
                "url": "https://www.udemy.com/topic/web-development/",
            },
            {
                "title": "Full Stack Open",
                "provider": "University of Helsinki",
                "url": "https://fullstackopen.com/",
            },
            {
                "title": "Epic React",
                "provider": "Kent C. Dodds",
                "url": "https://epicreact.dev/",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "Frontend fundamentals",
                "tasks": "Solidify HTML/CSS/JS, ship a React SPA.",
            },
            {
                "week": "Week 2",
                "focus": "Backend + DB",
                "tasks": "Build a Node.js REST API with PostgreSQL.",
            },
            {
                "week": "Week 3",
                "focus": "Auth + Deploy",
                "tasks": "Add JWT auth, deploy to Vercel + Railway.",
            },
            {
                "week": "Week 4",
                "focus": "System design",
                "tasks": "Add caching, CI/CD, tests, and monitoring.",
            },
        ],
    },
    "frontend": {
        "id": "frontend",
        "name": "Frontend Developer",
        "icon": "monitor",
        "description": "Craft polished, accessible, and performant user interfaces on the web.",
        "core_skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "TypeScript",
            "React",
            "Accessibility",
            "Responsive Design",
            "Testing",
            "Performance",
            "Git",
        ],
        "tools": ["React", "Next.js", "Tailwind CSS", "Vite", "Jest"],
        "projects": [
            "Pixel-perfect responsive marketing site",
            "Component library with Storybook",
            "Complex dashboard with data tables and charts",
            "Accessibility audit and remediation of an OSS site",
        ],
        "courses": [
            {
                "title": "The Joy of React",
                "provider": "Josh Comeau",
                "url": "https://www.joyofreact.com/",
            },
            {
                "title": "CSS For JS Devs",
                "provider": "Josh Comeau",
                "url": "https://css-for-js.dev/",
            },
            {
                "title": "Frontend Masters Path",
                "provider": "Frontend Masters",
                "url": "https://frontendmasters.com/",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "HTML/CSS mastery",
                "tasks": "Flexbox, Grid, responsive layouts, semantic HTML.",
            },
            {
                "week": "Week 2",
                "focus": "Modern JS + TS",
                "tasks": "ES6+, async, TypeScript basics, DOM APIs.",
            },
            {
                "week": "Week 3",
                "focus": "React + State",
                "tasks": "Hooks, context, React Query, Next.js routing.",
            },
            {
                "week": "Week 4",
                "focus": "Quality + Perf",
                "tasks": "Testing, a11y audit, Core Web Vitals tuning.",
            },
        ],
    },
    "backend": {
        "id": "backend",
        "name": "Backend Developer",
        "icon": "server",
        "description": "Design robust APIs, databases, and services that power modern applications.",
        "core_skills": [
            "Python or Node.js",
            "SQL",
            "REST",
            "GraphQL",
            "Auth",
            "Caching",
            "Message Queues",
            "Docker",
            "System Design",
            "Testing",
        ],
        "tools": [
            "FastAPI / Express",
            "PostgreSQL",
            "Redis",
            "RabbitMQ",
            "Docker",
        ],
        "projects": [
            "URL shortener with rate limiting and caching",
            "Job queue processor with Redis + workers",
            "Multi-tenant REST API with role-based auth",
            "Event-driven microservice with pub/sub",
        ],
        "courses": [
            {
                "title": "Designing Data-Intensive Applications",
                "provider": "Book",
                "url": "https://dataintensive.net/",
            },
            {
                "title": "FastAPI Complete Course",
                "provider": "Udemy",
                "url": "https://www.udemy.com/topic/fastapi/",
            },
            {
                "title": "System Design Primer",
                "provider": "GitHub",
                "url": "https://github.com/donnemartin/system-design-primer",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "APIs + DB",
                "tasks": "Ship a REST API in FastAPI/Express with PostgreSQL.",
            },
            {
                "week": "Week 2",
                "focus": "Auth + testing",
                "tasks": "JWT, RBAC, unit + integration tests.",
            },
            {
                "week": "Week 3",
                "focus": "Scaling",
                "tasks": "Add Redis caching, background jobs, message queue.",
            },
            {
                "week": "Week 4",
                "focus": "System design",
                "tasks": "Study high-traffic patterns, design a scalable service.",
            },
        ],
    },
    "java": {
        "id": "java",
        "name": "Java Developer",
        "icon": "coffee",
        "description": "Build enterprise-grade backend systems using Java and the Spring ecosystem.",
        "core_skills": [
            "Java",
            "Spring Boot",
            "Hibernate",
            "SQL",
            "REST APIs",
            "Maven",
            "JUnit",
            "OOP",
            "Microservices",
            "Design Patterns",
        ],
        "tools": [
            "Spring Boot",
            "Hibernate",
            "Kafka",
            "PostgreSQL",
            "IntelliJ",
        ],
        "projects": [
            "REST API for an e-commerce backend with Spring Boot",
            "Microservices with Spring Cloud + Eureka",
            "Kafka-driven event pipeline in Java",
            "Banking transaction service with JPA + Postgres",
        ],
        "courses": [
            {
                "title": "Spring & Hibernate for Beginners",
                "provider": "Udemy",
                "url": "https://www.udemy.com/topic/spring-framework/",
            },
            {
                "title": "Java Programming Masterclass",
                "provider": "Udemy",
                "url": "https://www.udemy.com/topic/java/",
            },
            {
                "title": "Effective Java",
                "provider": "Book / Bloch",
                "url": "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "Java core",
                "tasks": "OOP, collections, streams, exception handling.",
            },
            {
                "week": "Week 2",
                "focus": "Spring Boot",
                "tasks": "Build a REST API with Spring Boot + JPA.",
            },
            {
                "week": "Week 3",
                "focus": "Data + Testing",
                "tasks": "Hibernate, PostgreSQL, JUnit, Mockito.",
            },
            {
                "week": "Week 4",
                "focus": "Microservices",
                "tasks": "Split monolith, add Docker, Kafka, and CI.",
            },
        ],
    },
    "python": {
        "id": "python",
        "name": "Python Developer",
        "icon": "code",
        "description": "Ship robust Python services, automation, and data tooling for modern platforms.",
        "core_skills": [
            "Python",
            "OOP",
            "FastAPI",
            "Django",
            "SQL",
            "Pytest",
            "Async",
            "Docker",
            "REST APIs",
            "Git",
        ],
        "tools": ["FastAPI", "Django", "Celery", "Pytest", "Docker"],
        "projects": [
            "REST API with FastAPI + PostgreSQL + JWT auth",
            "Django blog with admin, auth, and deployment",
            "Async web scraper with rate limiting",
            "CLI tool published to PyPI",
        ],
        "courses": [
            {
                "title": "Python for Everybody",
                "provider": "Coursera",
                "url": "https://www.coursera.org/specializations/python",
            },
            {
                "title": "Test-Driven Development with FastAPI",
                "provider": "TestDriven.io",
                "url": "https://testdriven.io/",
            },
            {
                "title": "Two Scoops of Django",
                "provider": "Book",
                "url": "https://www.feldroy.com/books/two-scoops-of-django-3-x",
            },
        ],
        "roadmap": [
            {
                "week": "Week 1",
                "focus": "Python fluency",
                "tasks": "OOP, typing, async, packaging.",
            },
            {
                "week": "Week 2",
                "focus": "Web frameworks",
                "tasks": "Ship a FastAPI or Django app with tests.",
            },
            {
                "week": "Week 3",
                "focus": "Data + async",
                "tasks": "SQLAlchemy, Celery, background jobs.",
            },
            {
                "week": "Week 4",
                "focus": "Deployment",
                "tasks": "Dockerize, deploy, add CI + monitoring.",
            },
        ],
    },
}


COMMON_SKILLS_KEYWORDS: list[str] = [
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",
    "go",
    "rust",
    "ruby",
    "php",
    "kotlin",
    "swift",
    "scala",
    "r",
    "html",
    "css",
    "tailwind",
    "sass",
    "react",
    "next.js",
    "nextjs",
    "vue",
    "angular",
    "svelte",
    "redux",
    "node",
    "node.js",
    "nodejs",
    "express",
    "fastapi",
    "django",
    "flask",
    "spring",
    "spring boot",
    "hibernate",
    "rails",
    ".net",
    "sql",
    "mysql",
    "postgresql",
    "postgres",
    "mongodb",
    "redis",
    "sqlite",
    "oracle",
    "elasticsearch",
    "aws",
    "azure",
    "gcp",
    "google cloud",
    "docker",
    "kubernetes",
    "terraform",
    "ansible",
    "jenkins",
    "ci/cd",
    "github actions",
    "git",
    "linux",
    "bash",
    "rest",
    "graphql",
    "grpc",
    "kafka",
    "rabbitmq",
    "pandas",
    "numpy",
    "scikit-learn",
    "sklearn",
    "pytorch",
    "tensorflow",
    "keras",
    "matplotlib",
    "seaborn",
    "plotly",
    "tableau",
    "power bi",
    "excel",
    "looker",
    "machine learning",
    "deep learning",
    "nlp",
    "computer vision",
    "statistics",
    "a/b testing",
    "llm",
    "langchain",
    "openai",
    "hugging face",
    "vector database",
    "prompt engineering",
    "rag",
    "agile",
    "scrum",
    "jira",
    "junit",
    "pytest",
    "jest",
    "mocha",
    "cypress",
    "selenium",
    "microservices",
    "system design",
    "oop",
    "data structures",
    "algorithms",
]


class CareerState(rx.State):
    selected_role_id: str = "ai-engineer"
    resume_filename: str = ""
    resume_text: str = ""
    resume_error: str = ""
    is_extracting: bool = False
    upload_progress: int = 0
    detected_skills: list[str] = []

    @rx.var
    def role(self) -> RoleData:
        return ROLES.get(self.selected_role_id, ROLES["ai-engineer"])

    @rx.var
    def role_options(self) -> list[dict[str, str]]:
        return [
            {"id": r["id"], "name": r["name"], "icon": r["icon"]}
            for r in ROLES.values()
        ]

    @rx.var
    def has_resume(self) -> bool:
        return len(self.resume_text) > 50

    @rx.var
    def resume_word_count(self) -> int:
        return len(self.resume_text.split()) if self.resume_text else 0

    @rx.var
    def resume_char_count(self) -> int:
        return len(self.resume_text)

    @rx.var
    def missing_skills(self) -> list[str]:
        role_skills = self.role["core_skills"]
        detected_lower = {s.lower() for s in self.detected_skills}
        return [
            s
            for s in role_skills
            if s.lower() not in detected_lower
            and not any(
                s.lower() in d or d in s.lower() for d in detected_lower
            )
        ]

    @rx.var
    def matched_skills(self) -> list[str]:
        role_skills = self.role["core_skills"]
        detected_lower = {s.lower() for s in self.detected_skills}
        return [
            s
            for s in role_skills
            if s.lower() in detected_lower
            or any(s.lower() in d or d in s.lower() for d in detected_lower)
        ]

    @rx.var
    def readiness_score(self) -> int:
        if not self.has_resume:
            return 0
        total = len(self.role["core_skills"])
        if total == 0:
            return 0
        matched = len(self.matched_skills)
        return int((matched / total) * 100)

    @rx.var
    def readiness_label(self) -> str:
        s = self.readiness_score
        if s == 0:
            return "Not Assessed"
        if s < 35:
            return "Early Stage"
        if s < 60:
            return "Developing"
        if s < 80:
            return "Interview Ready"
        return "Strong Match"

    @rx.var
    def readiness_color(self) -> str:
        s = self.readiness_score
        if s == 0:
            return "gray"
        if s < 35:
            return "red"
        if s < 60:
            return "yellow"
        if s < 80:
            return "blue"
        return "green"

    @rx.event
    def set_role(self, role_id: str):
        if role_id in ROLES:
            self.selected_role_id = role_id

    @rx.event
    def clear_resume(self):
        self.resume_filename = ""
        self.resume_text = ""
        self.resume_error = ""
        self.detected_skills = []
        self.upload_progress = 0

    @rx.event
    def handle_upload_progress(self, progress: dict):
        self.is_extracting = True
        try:
            self.upload_progress = round(
                float(progress.get("progress", 0)) * 100
            )
        except Exception:
            logging.exception("Unexpected error")
            self.upload_progress = 0
        if self.upload_progress >= 100:
            self.is_extracting = False

    def _extract_skills(self, text: str) -> list[str]:
        found: list[str] = []
        lower = text.lower()
        seen: set[str] = set()
        for kw in COMMON_SKILLS_KEYWORDS:
            if kw in lower and kw not in seen:
                seen.add(kw)
                found.append(kw.title() if len(kw) > 2 else kw.upper())
        return found

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            self.resume_error = (
                "No file was selected. Please choose a PDF or TXT file."
            )
            return
        file = files[0]
        self.is_extracting = True
        self.resume_error = ""
        self.upload_progress = 0
        try:
            data = await file.read()
        except Exception as e:
            logging.exception(f"Error reading upload: {e}")
            self.resume_error = "Failed to read the uploaded file. Try again."
            self.is_extracting = False
            return

        max_size = 5 * 1024 * 1024
        if len(data) > max_size:
            self.resume_error = f"File is too large ({len(data) // 1024} KB). Maximum size is 5MB."
            self.is_extracting = False
            return
        if len(data) == 0:
            self.resume_error = "The uploaded file is empty."
            self.is_extracting = False
            return

        name = file.name or "resume"
        lower_name = name.lower()
        text = ""

        try:
            if lower_name.endswith(".pdf"):
                from pypdf import PdfReader

                reader = PdfReader(io.BytesIO(data))
                pages_text: list[str] = []
                for page in reader.pages:
                    try:
                        pages_text.append(page.extract_text() or "")
                    except Exception as e:
                        logging.exception(f"Error extracting page: {e}")
                text = "\n".join(pages_text).strip()
            elif lower_name.endswith(".txt"):
                try:
                    text = data.decode("utf-8", errors="ignore").strip()
                except Exception as e:
                    logging.exception(f"Error decoding txt: {e}")
                    self.resume_error = "Could not decode the text file. Ensure it is UTF-8 encoded."
                    self.is_extracting = False
                    return
            else:
                self.resume_error = (
                    "Unsupported file type. Please upload a .pdf or .txt file."
                )
                self.is_extracting = False
                return
        except Exception as e:
            logging.exception(f"Extraction failed: {e}")
            self.resume_error = "We could not read the content of your resume. Try a different file."
            self.is_extracting = False
            return

        if len(text) < 50:
            self.resume_error = "Extracted resume text is too short. Please upload a resume with readable content (PDF or TXT)."
            self.is_extracting = False
            return

        try:
            upload_dir = rx.get_upload_dir()
            upload_dir.mkdir(parents=True, exist_ok=True)
            (upload_dir / name).write_bytes(data)
        except Exception as e:
            logging.exception(f"Save error (non-fatal): {e}")

        self.resume_filename = name
        self.resume_text = text
        self.detected_skills = self._extract_skills(text)
        self.upload_progress = 100
        self.is_extracting = False

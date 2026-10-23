def generate_resume(name, career, skills):

    resume = f"""
===========================
        RESUME
===========================

Name: {name}

Career Goal: {career}

Skills:
"""

    for s in skills:
        resume += f"- {s}\n"

    resume += """

Projects:
- Career Roadmap Learning Project

Achievements:
- Completed Career Roadmap Training

Experience:
- Internship (Suggested by System)

===========================
"""

    return resume
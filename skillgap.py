def analyze_skill_gap():

    print("\n--- Skill Gap Analyzer ---")

    career = input("Enter your target career: ")

    student_skills = input("Enter your skills (comma separated): ")
    student_skills = [s.strip().lower() for s in student_skills.split(",")]

    career_skills = {
        "ai engineer": ["python", "machine learning", "deep learning", "tensorflow"],
        "web developer": ["html", "css", "javascript", "react"],
        "data scientist": ["python", "statistics", "machine learning", "pandas"],
        "cyber security": ["networking", "linux", "ethical hacking", "python"]
    }

    required = career_skills.get(career.lower(), [])

    missing = []

    for skill in required:
        if skill not in student_skills:
            missing.append(skill)

    print("\nMissing Skills:")

    for m in missing:
        print("-", m)
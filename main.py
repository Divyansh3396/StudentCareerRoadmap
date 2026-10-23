from linkedinpost import generate_linkedin_post
from internships import find_internships
from dashboard import show_dashboard
from skillgap import analyze_skill_gap
from degrees import degrees
from roadmap import roadmaps
from testsystem import start_test
from resume import generate_resume
from progress import save_progress

print("\nChoose an option:")
print("1. Take Career Test")
print("2. Generate Resume")
print("3. Skill Gap Analyzer")
print("4. Student Dashboard")
print("5. Internship Finder")
print("6. Generate LinkedIn Achievement Post")

choice = input("Enter choice: ")

if choice == "1":
    start_test()

elif choice == "2":
    generate_resume()

elif choice == "3":
    analyze_skill_gap()

elif choice == "4":
    show_dashboard()

elif choice == "5":
    find_internships()

elif choice == "6":
 generate_linkedin_post()
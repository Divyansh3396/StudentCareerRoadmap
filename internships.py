def find_internships():

    print("\n--- Internship Finder ---")

    career = input("Enter your career field: ").lower()

    internships = {
        "ai engineer": ["LinkedIn", "Kaggle", "Internshala"],
        "web developer": ["LinkedIn", "Internshala", "Indeed"],
        "data scientist": ["Kaggle", "LinkedIn", "Glassdoor"],
        "cyber security": ["LinkedIn", "HackTheBox", "Indeed"]
    }

    if career in internships:
        print("\nRecommended Internship Platforms:")

        for site in internships[career]:
            print("-", site)

    else:
        print("No internships found for this field yet.")
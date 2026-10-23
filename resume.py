def generate_resume():

    print("\n--- Resume Builder ---")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    skills = input("Enter your skills (comma separated): ")
    projects = input("Enter your projects: ")

    print("\n----- Generated Resume -----\n")

    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)

    print("\nSkills:")
    for skill in skills.split(","):
        print("-", skill.strip())

    print("\nProjects:")
    print(projects)

    print("\nResume Generated Successfully!")
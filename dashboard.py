import json

def show_dashboard():

    print("\n------ Student Dashboard ------")

    name = input("Enter your name: ")

    try:
        with open("database.json", "r") as file:
            data = json.load(file)

    except:
        print("No data found.")
        return

    if name not in data:
        print("No progress found for this student.")
        return

    student_data = data[name]

    print("\nStudent Name:", name)

    for branch in student_data:
        steps = student_data[branch]
        print("\nBranch:", branch)
        print("Completed Steps:", len(steps))
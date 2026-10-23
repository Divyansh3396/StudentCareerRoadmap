import json

def generate_linkedin_post():

    print("\n--- LinkedIn Achievement Generator ---")

    name = input("Enter your name: ")

    try:
        with open("database.json", "r") as file:
            data = json.load(file)

    except:
        print("No progress data found.")
        return

    if name not in data:
        print("Student data not found.")
        return

    print("\n🎉 Achievement Update!\n")

    for branch in data[name]:

        print(name, "has completed the following milestones in", branch)

        for step in data[name][branch]:
            print("✔", step)

    print("\nExcited to continue the journey toward career success! 🚀")
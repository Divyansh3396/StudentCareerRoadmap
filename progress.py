import json

def save_progress(name, branch, step):

    with open("database.json", "r") as f:
        data = json.load(f)

    if name not in data["progress"]:
        data["progress"][name] = {}

    if branch not in data["progress"][name]:
        data["progress"][name][branch] = []

    data["progress"][name][branch].append(step)

    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)

def show_progress(name):

    with open("database.json", "r") as f:
        data = json.load(f)

    if name in data["progress"]:
        print("\nYour Progress:")
        print(data["progress"][name])
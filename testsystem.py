def start_test():

    questions = [
        {
            "question": "Which language is used for AI?",
            "options": ["1. Python", "2. HTML", "3. CSS", "4. Excel"],
            "answer": "1"
        },
        {
            "question": "Which structure stores key-value pairs?",
            "options": ["1. List", "2. Dictionary", "3. Tuple", "4. Set"],
            "answer": "2"
        },
        {
            "question": "Which library is used for Machine Learning?",
            "options": ["1. NumPy", "2. TensorFlow", "3. Pandas", "4. All"],
            "answer": "4"
        }
    ]

    score = 0

    print("\nCareer Readiness Test\n")

    for q in questions:
        print(q["question"])

        for opt in q["options"]:
            print(opt)

        ans = input("Your answer: ")

        if ans == q["answer"]:
            score += 1
            print("Correct\n")
        else:
            print("Wrong\n")

    print("Your Score:", score, "/", len(questions))
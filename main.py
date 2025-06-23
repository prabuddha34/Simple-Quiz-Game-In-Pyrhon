questions = (" 1) When WWII ended?", " 2) When the moon landing happened?")
options = (
    ("A.1945", "B.1944", "C.1967", "D.1999"),
    ("A.1965", "B.1964", "C.1967", "D.1969")
)
answers = ["A", "D"]

guess = []
score = 0

for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    user_guess = input("Enter your answer (A, B, C, or D): ").upper()
    guess.append(user_guess)

    if user_guess == answers[i]:
        score += 1
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer was {answers[i]}.\n")

print(f"Your score is {score}/{len(questions)}")

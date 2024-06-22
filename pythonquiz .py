print("Welcome to my Quiz game")

question_blocks = [
    {"Q1": "What does pip stand for python?", "Answer": "C"},
    {"Q2": "Is Python case sensitive when dealing with identifiers?", "Answer": "B"},
    {"Q3": "Which of the following is used to define a block of code in Python language?", "Answer": "A"},
]

options = [
    ["A. Pip Installs Python", "B. Pip Installs Packages", "C. Preferred Installer Program", "D. All of the mentioned"],
    ["A. No", "B. Yes", "C. machine dependent", "D. none of the mentioned"],
    ["A. Indentation", "B. Key", "C. Brackets", "D. All of the mentioned"]
]

score = 0

def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_blocks)):
    question = question_blocks[question_num]
    for key in question:
        if key != "Answer":
            print(f"{key}: {question[key]}")
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, question["Answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
    print(f"The correct Answer is {question['Answer']}")
    print()

print(f"Your final score is {score}")
print(f"Your score is {(score/len(question_blocks))*100}%")
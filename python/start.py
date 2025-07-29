#scroll down to see the assignment code 
#A simple Python program that interacts with the user, asking for their name and favorite color,
# and then runs a quiz with multiple-choice questions.
"""name = input("Enter your name: ")
favourite_color = input("Enter your favourite color: ")
print(f"Hello, {name}! Your favourite color is {favourite_color}.")
def run_quiz():
    questions = [
        {
            "question": "What is the keyword to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },
        {
            "question": "Which movie features a character named Iron Man?",
            "options": ["A. Batman", "B. Avengers", "C. Spider-Man", "D. Superman"],
            "answer": "B"
        },
        {
            "question": "What does 'print()' do in Python?",
            "options": ["A. Takes input", "B. Loops data", "C. Outputs text", "D. Declares variables"],
            "answer": "C"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour score: {score}/{len(questions)}")

def main():
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

main()"""
#Above is a simple Python program that interacts with the user, asking for their name and favorite color, 
# and then runs a quiz with multiple-choice questions. 
# The user can play the quiz multiple times if they wish.

#below is the code for a simple calculator that performs basic arithmetic operations based on user input.
#it's for the assignment from the lms
operation_math = input(" Write two numbers and the mathematical operation you want to perform (e.g., 5 + 3): ")
try:
    num1, operator, num2 = operation_math.split()
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"
    print(f"The result of {num1} {operator} {num2} is: {result}")
except Exception as e:
    print(f"Error: {e}")
print("Thank you for using the calculator!")
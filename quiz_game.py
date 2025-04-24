# Import required modules
import time  # For time-related functions like sleep
import random  # For shuffling questions

# Function to return a list of Python quiz questions with options and answers
def get_python_questions():
    return [
        {"question": "Which keyword is used to define a function in Python?",
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
        
        {"question": "What is the output of print(2 ** 3) in Python?", 
         "options": ["A) 6", "B) 8", "C) 9", "D) 10"], "answer": "B"},
        
        {"question": "Which data type is mutable in Python?", 
         "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], "answer": "C"},
        
        {"question": "Which of the following is used to take input from the user?", 
         "options": ["A) input()", "B) print()", "C) scan()", "D) read()"], "answer": "A"},
        
        {"question": "What will be the output of len('Python')?",
         "options": ["A) 5", "B) 6", "C) 7", "D) Error"], "answer": "B"}
    ]

# Function to display a 10-second countdown timer
def countdown_timer():
    print("\nYou have 10 seconds to think...")
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(f"\rTime left: {i} seconds ", end="")  # \r to overwrite the line
        time.sleep(1)  # Pause for 1 second between counts
    print("\n")  # New line after countdown

# Function to display a question and its options
def display_question(question_data, question_number):
    print("\n====================")
    print(f"Question {question_number}: {question_data['question']}")  # Print question number and text
    for option in question_data["options"]:  # Print each option
        print(option)

# Function to get and validate user's answer
def get_user_answer():
    user_answer = input("Now enter your answer (A, B, C, D): ").strip().upper()  # Get and clean input
    if user_answer in ["A", "B", "C", "D"]:  # Check if answer is valid
        return user_answer
    else:
        return None  # Return None for invalid answers

# Function to check if user's answer matches correct answer
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Answer is correct!")
        return 1  # Return 1 for correct answer
    else:
        print(f"Your answer is wrong! the correct answer is {correct_answer}.")
        return 0  # Return 0 for wrong answer

# Function to update the score based on answer result
def update_score(score, result):
    if result == 1:  # If answer was correct (result = 1)
        score += 1  # Increment score by 1
    return score  # Return updated score
    
# Main function to run the quiz
def play_quiz():
    print("Welcome to Python Quiz!")
    questions = get_python_questions()  # Get all questions
    random.shuffle(questions)  # Shuffle questions for random order
    score = 0  # Initialize score
    i = 1  # Initialize question counter

    # Loop through each question
    for question in questions:
        display_question(question, i)  # Show current question
        countdown_timer()  # Start countdown
        user_answer = get_user_answer()  # Get user's answer
        result = check_answer(user_answer, question["answer"])  # Check answer
        score = update_score(score, result)  # Update score
        i = i + 1  # Increment question counter

    # Display final results
    print(f"Your final score is: {score} / {len(questions)}")
    print("Thanks for playing!")

# Entry point of the program
if __name__ == "__main__":
    play_quiz()  # Start the quiz

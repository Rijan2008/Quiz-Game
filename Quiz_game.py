""" File name: Quiz_game.py
    Description: A simple quiz game about computer-related questions
    Author: Rijan Adhikari 
    Date: 2026/06/20  
    Purpose: To test the user's knowledge about computer-related topics and provide a fun and in interactive way to learn about computers. 
            The quiz consists of 5 questions, and the user's score is calculated based on their answers.           
"""


print("Welcome to Rijan's quick quiz!\n")

playing = input("Do you want to play quick computer related quiz game? (Yes/No) ")


if playing.lower() != "yes":
    quit() # if we type anything other than "yes" then the program will quit automatically 
print("Okay! Let's play! \n")

user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Let's get started. \n")

score = 0 # initial score is 0
print("Your initial score is 0/5 \n")

#  -- Question 1 --
Q1_question = print("What does CPU stand for?")
Q1_answer = "central processing unit"
Q1_hint = "It is known as the brain of the computer."

user_guess = input("Your answer: ").lower()
if user_guess == Q1_answer:
    print("Correct! \n")
    score += 1
    print(f"Your current score is {score}/5 \n")
else:
    print("Wrong! \n")

# -- Question 2 --
Q2_question = print("What does RAM stand for?")
Q2_answer = "random access memory"
Q2_hint = "It is the temporary storage space in a computer."

user_guess = input("Your answer: ").lower()
if user_guess == Q2_answer:
    print("Correct! \n")
    score += 1
    print(f"Your current score is {score}/5 \n")
else:
    print("Wrong! \n")

# -- Question 3 --
Q3_question = print("What does ROM stand for?")
Q3_answer = "read only memory"
Q3_hint = "It is the permanent storage space in a computer."

user_guess = input("Your answer: ").lower()
if user_guess == Q3_answer:
    print("Correct! \n")
    score += 1
    print(f"Your current score is {score}/5 \n")
else:
    print("Wrong! \n")

# --Question 4 --
Q4_question = print("What does GPU stand for?")
Q4_answer = "graphics processing unit"
Q4_hint = "It is responsible for rendering images and graphics in a computer."

user_guess = input("Your answer: ").lower()
if user_guess == Q4_answer:
    print("Correct! \n")
    score += 1
    print(f"Your current score is {score}/5 \n")
else:
    print("Wrong! \n")

# Question 5 --
Q5_question = print("What programming language are you using right now to answer these questions? ")
Q5_answer = "python"
Q5_hint = "It is a high-level programming language."

user_guess = input("Your answer: ").lower()
if user_guess == Q5_answer:
    print("Correct! \n")
    score += 1
    print(f"Your Final score is {score}/5 \n")
    print(f"Congraluation {user_name}! You have completed the quiz with a score of {score}/5 \n")
else:
    print("Wrong! \n")


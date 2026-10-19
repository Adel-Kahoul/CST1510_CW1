"""
Task 2: Multiplication Quiz
Suppose you want to develop a program to help a first-grader practice multiplication. The program randomly generates two single-digit integers, number1 and number2, and displays to the student a question such as: What is 1 * 7. After the student types the answer, the program displays a message to indicate whether it is true or false.

To generate a random number, you can use the randint(a, b) function in the random module. This function returns a random integer i between a and b, inclusively. To obtain a random integer between 0 and 9, use randint(0, 9).

The program may be set up to work as follows:

Step 1: Randomly generate two single-digit integers for number1 (e.g., 4) and number2 (e.g., 5)
Step 2: Prompt the student to answer, "What is 4 * 5?" (user input)
Step 3: Check whether the student's answer is correct.
"""
import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = int(input(f"What is {number1} * {number2}? "))

if answer == number1 * number2:
    print(f"{number1} * {number2} = {answer} is True")
else:
    print(f"{number1} * {number2} = {answer} is False")
"""
Task 1: Questionnaire
Write a program that asks for name, interest, nationality, course, and programming experience, then prints a formatted summary using escape sequences (\n, \t).

Example Output:

User Information:
	Name: Alice
	Interest: Security
	Nationality: UK
	Course: Cyber
	Experience: Beginner
"""
name = input("What is your name? ")
interest = input("What is your interest? ")
nationality = input("What is your nationality? ")
course = input("What is your course? ")
experience = input("What is your programming experience? ")

print("User Information:")
print("\tName: " + name)
print("\tInterest: " + interest)
print("\tNationality: " + nationality)
print("\tCourse: " + course)
print("\tExperience: " + experience)
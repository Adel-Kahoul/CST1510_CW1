"""
Task 1: Reverse Input
Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read, your program should display them (except for the 0) in reverse order, with one value appearing on each line.
"""
numbers = []

value = int(input("Enter an integer (0 to finish): "))
while value != 0:
    numbers.append(value)
    value = int(input("Enter an integer (0 to finish): "))

for number in reversed(numbers):
    print(number)
"""
Task 3: Even or Odd
Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.


"""
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
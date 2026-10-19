"""
Task 4: Lottery Ticket
In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random selection of 6 numbers for a lottery ticket. Display the numbers in ascending order.
"""
import random

ticket = random.sample(range(1, 50), 6)
ticket.sort()

print("Your lottery numbers:", ticket)
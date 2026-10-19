"""
Task 2: Dice Throws
Create a list of seven dice throws.

The throws should be randomly generated and added to the list.
Shuffle the list and print it out.
Sort the list in descending order and print it out.
Count the occurrences and print them out.
"""
import random

throws = []
for _ in range(7):
    throws.append(random.randint(1, 6))

random.shuffle(throws)
print("Shuffled:", throws)

throws.sort(reverse=True)
print("Sorted (descending):", throws)

for face in range(1, 7):
    print(f"{face} appears {throws.count(face)} time(s)")
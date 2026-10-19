"""
Task 3: Convert Pounds to Kilograms
Ask the user for a value in pounds, convert to kilograms using 1 lb = 0.454 kg, and print the result.

Example Output:

55.5 pounds is 25.197 kilograms
"""
pounds = float(input("Enter a weight in pounds: "))

kilograms = pounds * 0.454

print(f"{pounds} pounds is {kilograms:.3f} kilograms")
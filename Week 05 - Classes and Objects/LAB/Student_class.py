"""
Create a class Student with attributes name and age set in __init__. Create two student objects and print their attributes using dot notation.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Tony", 18)
student2 = Student("Christopher", 19)

print(student1.name, student1.age)
print(student2.name, student2.age)
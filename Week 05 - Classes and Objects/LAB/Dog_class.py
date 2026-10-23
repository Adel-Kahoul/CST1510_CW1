"""
Create a class Dog with name and age, and two methods:

bark() prints " says Woof!"
birthday() increases the dog's age by 1
Create a dog, call bark(), call birthday() twice and print the new age.
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says Woof!")

    def birthday(self):
        self.age += 1


my_dog = Dog("Silvio", 3)

my_dog.bark()
my_dog.birthday()
my_dog.birthday()
print(my_dog.age)
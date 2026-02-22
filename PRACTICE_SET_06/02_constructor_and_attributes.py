'''Create a class Person with a constructor(__init)__) that accepts name and age as argumetns and stores them as instance attributes.
Create an object and print the person's name and age.'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
p1 = Person("Arun", 20)
p1.print_person()
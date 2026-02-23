class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    @first_name.setter()
    def change_first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        return new_name
    
e = Employee("Chanaswamy Iyer", 823498)

# print(e.first_name())
# print(e.change_first_name("Mutuswamy"))

print(e.first_name)
e.first_name = "John"
print(e.name)
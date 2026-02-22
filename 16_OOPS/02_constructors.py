class Employee:
    def __init__(self, name, salary, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
        return self.salary 

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

    
e1 = Employee("Bob",32459,  4)
e1.get_info()
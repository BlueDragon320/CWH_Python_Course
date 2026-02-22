class Employee:
    company = "Lenovo"
    def __init__(self, name, salary, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self):
        return self.salary 

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

    
e1 = Employee("Bob",32459,  4, "Tesla")
print(e1.company)
print(Employee.company)

print(dir(e1))
class Employee:
    company = "Lenovo"
    
    def get_salary(self):
        return 99999
    
e = Employee()
print(e.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)
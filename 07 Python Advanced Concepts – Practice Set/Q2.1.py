# 2. Getters and Setters

# Create a class Employee with a private attribute _salary .
# Use @property to define a getter for salary .

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
emp = Employee(50000)
print(emp.salary)
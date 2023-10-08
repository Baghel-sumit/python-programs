class Employee:
    salary = 89
    name = 'sumit'

    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def getSalary(self):
        return self.salary


rohan = Employee("Sumit", 3948)
print(rohan.salary)
print(rohan.name)
sumit = Employee("Suharmit", 3948456567)
print(sumit.salary)
print(sumit.name)

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return (22 / 7) * self.r**2

    def pmeter(self):
        return 2 * (22 / 7) * self.r


c1 = Circle(21)
print(c1.area())
print(c1.pmeter())


# q2 define Employee class with attributes role, dment, salary


class Employee:
    def __init__(self, role, dment, salary):
        self.role = role
        self.dment = dment
        self.salary = salary

    def showDetails(self):
        return self.role, self.dment, self.salary


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("HOD","IT",100000)

    # def __init__(self, name, age, role, dment, salary):
    #     self.name = name
    #     self.age = age
    #     super().__init__(role, dment, salary)

    def Sd(self):
        return (
            self.role,
            self.dment,
            self.salary,
            # self.showDetails(),
            self.name,
            self.age,
        )  


# employee class
e1 = Employee("Manager", "IT", 90000)
e2 = Employee("Head", "Sales", 70000)

# print(e1.showDetails())
# print(e2.showDetails())


# Engineer class

# eg1 = Engineer("Software Eng", "IT", 90000, "Tony", 26)
# print(eg1.Sd())

eg2= Engineer("Tony", 30)
print(eg2.Sd())

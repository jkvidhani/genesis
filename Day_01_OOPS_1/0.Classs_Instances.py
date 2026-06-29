# Say we had a application for company,
# and we wanted to [represent] our employees and pyhton code:
class employee:

    numOfEmp=0
    raise_amount= 1.04

    #emp_1/emp_2 == self
    def __init__(self,firstName,lastName,pay):
        self.f = firstName
        self.l = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

        employee.numOfEmp +=1 

    # METHOD
    def fullname(self):
        return '{} {}'.format(self.f , self.l)
    
    def apply_raise(self):
        self.pay = int( self.pay * self.raise_amount )#or employee.raise_amount

#own unique instances of emp class
emp_1= employee('Jai' ,'Dad' ,60000)
emp_2= employee('Test' ,'User' ,50000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(employee.fullname(emp_1)) # callinng method with CLASS so we give ((instance))
print(emp_1.fullname()) # calling method with instance it consider((self)) as instance automatically
print(emp_2.fullname())

# CLASS Variable
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(employee.numOfEmp)

# if instance dont contain any attribute but CLASS conatain and if we call that attribute by instance then if instance conatian that attribute it will be return otherwise if its associated CLASS conatain that then that will be printed
print(employee.__dict__)
print(employee.raise_amount)

print(emp_1.__dict__)
print(emp_1.raise_amount)

emp_2.raise_amount = 1.05
print(emp_2.__dict__)
print(emp_2.raise_amount)










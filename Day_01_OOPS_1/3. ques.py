# Q.1
class Student:

    def __init__(self,name,rno,marks):
        self.name = name
        self.rno = rno
        self.marks = marks

    def get_grade(self):

        if self.marks > 90:
            print("A")
        elif self.marks > 70:
            print("B")
        elif self.marks > 50:
            print("C")
        else:
            print("F")

    def display_info(self):
        return (self.name, self.rno, self.marks)


s1 = Student("Hulk",14,91)
s2 = Student("Antman",12,89)

s1.get_grade()
print(s1.display_info())
s2.get_grade()
print(s2.display_info())




# Q.2

class Account:
    def __init__(self,bal,acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self,amount):
        
        self.bal -= amount
        print("Rs.",amount ,"was debited")
        print("Total balance:", self.balance())


    def credit(self,amount):

        self.bal += amount
        print("Rs.",amount ,"was credited")
        print("Total balance:", self.balance())


    def balance(self):
        return self.bal




a1 = Account(10200, 143)

print(a1.bal,a1.acc_no)

a1.credit(300)
a1.debit(500)
print(a1.balance())



# Q.3

class Car:
    
    def __init__(self,brand,model,Cspeed):
        self.brand = brand
        self.model = model
        self.Cspeed = Cspeed

    def accelerate(self,speed):
        
        self.Cspeed += speed
    
    def brake(self):
        self.Cspeed -= 25

    def display(self):
        return self.brand, self.model, self.Cspeed


c1 = Car("BMW","M4 Competition",250)
c2 = Car("RR", "PhantomX", 150)

c1.accelerate(50)
c1.brake()
print(c1.display())

c2.accelerate(50)
c2.brake()
print(c2.display())


        

        

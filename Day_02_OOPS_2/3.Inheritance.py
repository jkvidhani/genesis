
# ✨Inheritance -> When one class(child/derived) derives the properties & methods from another class(parent/base)
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stoped...")

class ToyotaCar(Car):               #Single Inheritance
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):          #Multi-level Inheritance
    def __init__(self,type):
        self.type = type
    
c1= ToyotaCar("Fortuner")

#Single Inheritance
print(c1.color)
print(c1.brand)
c1.start()

#Multi-level Inheritance
c2= Fortuner("Petrol")
print(c2.type)

print("-----------------")


class A:                    #Multiple Inheritance
    varA= "wlcm A"
class B:
    varB= "wlcm B"
class C(A,B):
    varC= "wlcm C"

#Multiple Inheritance
c1= C()
print(c1.varC)
print(c1.varA)
print(c1.varB)
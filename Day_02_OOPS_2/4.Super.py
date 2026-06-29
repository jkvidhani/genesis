class Car:
    color = "Black"

    def __init__(self,type):
        self.type = type

    @staticmethod       #common method of class
    def start():
        print("Car Started...")

    @staticmethod       #common method of class
    def stop():
        print("Car Stoped...")

class ToyotaCar(Car):                #Single Inheritance
        def __init__(self,name,type):
            self.name = name
            super().__init__(type) #or self.type
            super().start()


car1= ToyotaCar("Fortuner","Petrol")

print(car1.name)
print(car1.type)
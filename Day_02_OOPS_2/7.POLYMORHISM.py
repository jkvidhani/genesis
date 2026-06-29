# Polymorphism = Operator overloading
# when the same operator having diff meanig acc to context
#DUNDER FUNC == [ __ ] ex = a.__(b)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print (self.real, "i +" ,self.img, "j")

    def __add__(self, c2):
        newR = self.real + c2.real
        newImg = self.img + c2.img
        return Complex(newR , newImg)
    def __sub__(self, c2):
        newR = self.real - c2.real
        newImg = self.img - c2.img
        return Complex(newR , newImg)
    
    #Dunder Functions:
    #__init__(self, other)
    # __add__(self, other)
    # __sub__(self, other)
    # __mul__ (self, other)
    # __truediv__(self, other)
    # __mod__(self, other[, modulo])
    #etc

 
c1= Complex(1,3)
c1.showNum()

c2= Complex(4,7)
c2.showNum()

#adding
# c3= c1.add(c2)
c3 = c1 + c2
c3.showNum()

#subtract
c4 = c1 - c2
c4.showNum()



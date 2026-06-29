class std:
    def __init__(self,chem,math,eng):
        self.chem = chem
        self.math = math
        self.eng = eng

    @property
    def percentage(self):
        return str((self.chem + self.math + self.eng) / 3) + "%"
    

s1= std(97,98,99)
print(s1.percentage)

# here if we have to make correction like chem marks are 100 not 97 then we write
s1.chem = 100
# now we have made (percentage) function a property therfore any change we made it will change in property 
# so its imp to use @property to make a func -> property, for auto changes in function
# ✨ We use property in attrib utes which are consist of Calculations
print(s1.percentage)
# create a class that take name and marks of 3 subject and return their avg:

class std:

    def __init__(self,name,marks):
        
        self.name= name
        self.marks= marks

    def  avg(self):

        sum=0
        for i in self.marks:
            sum+=i
        
        print("Hi", self.name ,"your avg score is:", sum/3)
        

    
s1= std("Tony", [99,100,101])
s1.avg()

s1.name="Irnoman"
s1.avg()

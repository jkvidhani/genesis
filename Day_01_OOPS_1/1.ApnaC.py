class student:

    numOfStd = 0

    collegeName = "ABC"    #CLASS Attribute

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

        student.numOfStd += 1

    #METHODS
    def wlcm(self):
        print("Welcome ",self.name)

    def get_marks(self):
        return self.marks
    
    # STATIC METHOD
    @staticmethod
    def hello():
        print("Hello")
    
    

s1 = student("Jai",101)  #object
s2 = student("Gojo",99)

print("Total std = ",student.numOfStd)

print(s1.name,s1.marks)
print(s1.collegeName, student.collegeName)
print(s2.name,s2.marks)

#METHODS
s1.wlcm()
print(s1.get_marks())

#STATIC METHOD
s1.hello()
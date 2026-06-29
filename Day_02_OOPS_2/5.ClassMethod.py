class Person:
    name = "A"

# to change class attribute permanently:

 #1
    # def chname(self,name):
    #     self.__class__.name = name
    #         # ✨ or
    #     Person.name = name

 #2
    @classmethod
    def chname(cls, name):    #✨ cls == class = Person
        cls.name = name



# crating object
p1 = Person()  

#calling and printing attribute w/o calling method
print(p1.name)
print(Person.name)

#calling method (changes applied to `CLASS`)
p1.chname("Stark")

#printing after calling  method
print(p1.name)
print(Person.name)

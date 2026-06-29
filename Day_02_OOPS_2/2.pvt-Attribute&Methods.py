class User:
    __name = "Anony"  # private Attribute -> we use ✨( __ ) to make pvt attribute

    def __hello(self):  # -> we use ✨( __ ) to make pvt method
        print("Hello")

    # ✨ pvt att and methods are meant to be used only within the class and are not accessible outside the class

    def wlcm(self):
        User.__hello()


u1 = User()
print(u1.__hello())  # wont run coz __hello() is private attribute
u1.wlcm()  # we defined another public method to use private method within the class and then call public attribute to access __hello()

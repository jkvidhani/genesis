# Let's Practice
# Qs. Create a class called Order which stores item & its price.
# Use Dunder function gt () to convey that:
# order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item= item
        self.price= price

    def __gt__(self, o2):
        return self.price > o2.price



o1= Order("Chips",20)
o2= Order("Tea",10)

print(o1 > o2) # (>) is executed w/o error bcoz of (__gt__)
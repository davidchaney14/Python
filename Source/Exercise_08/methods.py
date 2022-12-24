# Class Template by David Chaney
# Based on work by JOR
# Revision History
# 26102022 - Alpha
# Define a class object attribute, it will be the same for any instance of the class

class MyTemplate():
    # Constructor, part 2 called whenever an instance of the class is created
    semi_major_axis = 6378137
    semi_minor_axis = 6356752
    def __init__(self, attribute1: str, attribute2: bool, attribute3: bool) -> None:
        print("Constructore 2 ran")
    # Take in an arguement and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2
        self.attr3 = attribute3
    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")
    def my_method2(self):
        if self.attr3:
            print(f"Testing if the var is Bool + True then this is {self.attr3}")
        else:
            print(f"Testing and is false then this is also {self.attr3}")
    def my_method3(self, my_name:str):
        if self.attr3:
            print(f"Good morning {my_name}")
        else:
            print(f"False you are not {my_name}")

# Instantiate the class
my_object = MyTemplate("David", True, False)
# Check the object and type 
print(my_object.semi_major_axis, my_object.semi_minor_axis)
print(my_object.attr1, my_object.attr2)

my_object.my_method1()
my_object.my_method3("David")
my_object.my_method2()
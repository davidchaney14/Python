# Class Template by David Chaney
# Based on work by JOR
# Revision History
# 26102022 - Alpha
# Define a class object attribute, it will be the same for any instance of the class

class MyTemplate():
    # Constructor, part 2 called whenever an instance of the class is created
    semi_major_axis = 6378137
    semi_minor_axis = 6356752
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructore 2 ran")
    # Take in an arguement and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

# Instantiate the class
my_object = MyTemplate("David", True)
# Check the object and type 
print(my_object.semi_major_axis, my_object.semi_minor_axis)
print(my_object.attr1, my_object.attr2)
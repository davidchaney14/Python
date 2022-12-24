# Class Template by David Chaney
# Based on work by JOR
# Revision History
# 26102022 - Alpha

class MyTemplate():
    # Constructor, part 2 called whenever an instance of the class is created
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructore 2 ran")
    # Take in an arguement and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

# Instantiate the class
my_object = MyTemplate("David", True)
# Check the object and type 
print(type(my_object))
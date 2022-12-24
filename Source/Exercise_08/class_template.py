# Exercise end of page 7
# David Chaney
# 26102022
# Create and document a template for your own use, such that whenever you need a simple class, you can just copy the source code

# Define a class object

# Instantiate the class

class MyTest():
    
    # Constructor
    def __init__(self, test1: bool, test2: bool, test3: bool) -> None:
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
    
    # Method
    def my_method1(self):
        if self.test1:
            print(f"Self.Test1 is {self.test1}")
        else:
            print(f"Self.Test1 is actually {self.test1}")

# Instantiate the class
my_test = MyTest(False, True, False)

my_test.my_method1()

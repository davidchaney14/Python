# My Own Example
# David Chaney

# Create a class
class davidsWelcomeClass():

    # Constructor
    def __init__(self, my_greeting):
        print("Running constructor for davidsWelcomeClass")
        # Create attributes and set values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = davidsWelcomeClass("Morning and Welcome David!")
my_class1.my_method()
print(type(my_class1))
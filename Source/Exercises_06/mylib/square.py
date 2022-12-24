# Check if call is direct or remote and then act accordingly
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    square_text = "Yo, time to square stuff!"
    print(f"This module is called {__name__} and is being called by another script")
    def square(x):
        return x*x
    print(square(2))
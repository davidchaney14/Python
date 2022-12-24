# Check if call is direct or remote and then act accordingly
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    cube_text = "Yo, time to cube stuff!"
    print(f"This module is called {__name__} and is being called by another script")
    def cube(x):
        return x*x*x
    print(cube(2))
# Directory Utlities Stirkes Again!
# David Chaney
# 29102022
# Code gracefully robbed from JOR!

import os, platform, sys

# Define global vars
current_working_directory = None

def detect_os()->str:
    # Detect OS
    return platform.system()

def detect_working_directory()->str:
    # Detecy working Dirctory
    return os.getcwd()

if (__name__=="__main__"):
    # Check OS in use, lower case it !
    my_os = detect_os()
    my_os = my_os.lower()

    # Parse responce
    if my_os =="windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"UnIded System {my_os}")
        sys.exit()

    # Get current directory
    current_working_directory = detect_working_directory()
    print(f"Your working in {current_working_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")
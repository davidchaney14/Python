"""
directory_utilities.py
By : DC
Date : 22102022
"""

import os, sys, platform

# Define global vars 
current_working_dir = None

def detect_os()-> str:
    # Detect the OS in use
    return platform.system()

def detect_working_directory()->str:
    # Returns the directory this script was run from
    return os.getcwd()

if (__name__=='__main__'):
    print(f"This module executes as a indivducal script")

    # Check OS in use
    my_os = detect_os()
    my_os = my_os.lower()

    # Parse the response, only check for Windows/Linux
    if my_os == "windows":
        print(f"Your system is Windows")
    elif my_os == "linux":
        print(f"Your system is Liunux")
    else:
        print(f"Cannot continue, unknown system type ={my_os}")
        sys.exit()

    # Get the current working directory
    current_working_dir = detect_working_directory()
    print(f"Your are working from :{current_working_dir}")

else:
    print(f"This module is call {__name__} and is being called by another script")


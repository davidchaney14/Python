# OS Utilities
# EX 10
# 29/10/2022

import platform, psutil


def detect_os()->str:
    # Detect OS
    return platform.system()

if (__name__ == '__main__'):
    print(f"Module is called {__name__} and is standalone script")

    # Check OS in use
    my_os = detect_os()
    my_os = my_os.lower()

    # Parse response 
    if my_os == "windows":
        print("System is Windows")
    elif my_os == "linux":
        print("System is Linux")
    elif my_os == "darwin":
        print("System is MACOS")
    elif my_os == "cygwin":
        print("System is MACOS")
    elif my_os == "aix":
        print("System is IBM")
    else:
        print(f"UNID SYS = {my_os}")
else:
    pass

def cpu_load():
    # Return significant numbers relating to the CPU
    return(psutil.cpu_count(), psutil.cpu_percent())
    
#print(f"Number of CPUs: {psutil.cpu_count()}" )
#print(f"CPU load: {psutil.cpu_percent()}")
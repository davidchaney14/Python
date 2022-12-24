from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load
from time import sleep
#import os

# Check OS in use
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")
#print(log_path + filename)

# Loop forever!!!
while True:
    # Sleep 1 sec
    sleep(1)
    # Get time stamp
    timestamp = log_file_name("")
    # Get some info
    information = cpu_load()
    # Create line for logfile, conver the int to str
    logline = timestamp + ":" + str(information[0])+","+ str(information[1]) + "\n"
    # Try write to file
    try:
        #if not os.path.exists(log_path):
        #    os.makedirs(log_path)

        with open(filename, "a") as file_handle:
            print(f"logging to {filename}")
            file_handle.write(logline)
    except IOError as err:
        print(f"IO Error was {err}")
    except EOFError as err:
        print(f"EOF Error was {err}")
    except OSError as err:
        print("OS Error")
    except:
        print("General Error")

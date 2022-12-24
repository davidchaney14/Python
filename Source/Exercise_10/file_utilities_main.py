from file_utilities import path_name, log_file_name
from os_utilities import detect_os
import psutil

# Check OS in use
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".log")
print(log_path + filename)

def cpu_load():
    # Return significant numbers relating to the CPU
    return(psutil.cpu_count(), psutil.cpu_percent())
    
print(f"Number of CPUs: {psutil.cpu_count()}" )
print(f"CPU load: {psutil.cpu_percent()}")
    
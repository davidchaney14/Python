# File Utilities
# EX 10
# 29/10/2022

from datetime import datetime as dt
import sys, csv 

def path_name():
    # OS linked stuff
    this_os = sys.platform
    if this_os == 'win32':
        return './logfiles'
    elif this_os == 'linx':
        return '/home/pi/logfiles'
    else:
        print(f"UNID OS: {this_os}")
        exit(0)

def log_file_name(extension):
    # Creat file name in logfiles dir, based on current date and time
    # Requires RTC or Sync Clock
    now = dt.now()
    # Linux
    file_name = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    return file_name + extension

if (__name__ == '__main__'):
    print(f"Module is called {__name__} and is standalone script")
    log_path = path_name()
    filename = log_file_name(".log")
    print(log_path + filename)
else:
    pass
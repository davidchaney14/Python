from datetime import datetime as dt
# Get the current time in format YYYY-MM-DD HH:MM:SS:MSMSMSMS
today = dt.now()
print(today)
# Get Unix time in format 
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

weekday = dt.now().strftime("%A")
month = dt.now().strftime("%B")

print(f"{weekday}")
print(month)

# Excerise
year = dt.now().strftime("%Y")
hour = dt.now().strftime("%H")
min = dt.now().strftime("%M")
sec = dt.now().strftime("%S")

#all = dt.now().strftime()

print(year)
print(hour)
print(min)
print(sec)

# Human readable
print(f"The year is {year} this month is {month} today is {weekday} the time now is {hour}:{min}:{sec}")

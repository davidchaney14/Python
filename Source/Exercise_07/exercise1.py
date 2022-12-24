# Function to calculate remaining in endurance in minutues
# Endurance = fuel/fuel comsumption

# Declare vars 

fuel = 0
fuel_consumption = 10

def endurance_cal():
    while True :
        try:
            endurance = fuel/fuel_consumption
        except:
            # Bad value
            endurance == 0
            print("Error out of fuel")
            continue
        else:
            print(endurance)
            break
        finally:
            # After except, continue
            print()

endurance_cal()

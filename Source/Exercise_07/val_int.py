def validate_integer():
    # Loop forever
    while True:
        try:
            user_input = int(input("Enter an integer value: "))
        except:
            # Bad value
            print("Error")
            continue
        else:
            print("Valid Input")
            # Good value, exit the loop
            break
        finally:
            # After except, continue
            print("Try again - enter an integer value only")

validate_integer()
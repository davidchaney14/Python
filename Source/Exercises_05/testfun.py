# Item 1
def name_of_function(first_name):
	#Simple Test Function
	print(f"Yoo hoo, hell {first_name}")
	
name_of_function("JOR")

# Item 2 
def calculate_circimference(radius):
    # Radius Calc
    return 2 * 3.142 * radius
    
a = calculate_circimference(5)
print(a)

# Item 3
def calculate_circimference(radius = 3):
    # Radius Calc
    return 2 * 3.142 * radius
    
a = calculate_circimference()
print(a)

# Item 4
def calculate_circimference(radius):
    # Radius Calc take input from user
    return 2 * 3.142 * radius
    
# Get input
r = input("Provide your radious value: ")
r_float = float(r)
# Call function
a = calculate_circimference(r_float)
print(a)

# Item 5 
def auto_adder(*my_numbers):
    final_number = 0 
    for number in my_numbers:
        final_number=final_number + number
    return final_number
    
print(auto_adder(12,34,23,66,8,99))

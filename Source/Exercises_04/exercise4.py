# Kelvin to Celsius & Fahrenheit converter

# Start with list of ten Kelvin values

my_kelvin_values_list = [0, -100, -200, -300, 400, 500, 600, 700, 800, 900, 487]

# Lets start just with Celsius
# Celsius = (Kelvin – 273.15)

# Start with converstion for Celsius
converstion_1 = 273.15

kelvin_to_celsius = [(kelvin_value - converstion_1) for kelvin_value in my_kelvin_values_list]

print (kelvin_to_celsius)

# Converstion to Fahrenheit
# Fahrenheit = (Kelvin - 459.67)

converstion_2 = 459.67

kelvin_to_fahrenheit = [(kelvin_value - converstion_2) for kelvin_value in my_kelvin_values_list]

print (kelvin_to_fahrenheit)
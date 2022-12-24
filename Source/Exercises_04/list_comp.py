#part 1
my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)
print(my_list)

#part 2
my_list = [letter for letter in my_string]
print (my_list)

#part 3
my_list = [number for number in range (0,20)]
print (my_list)

#part 4
my_list = [number * 10 for number in range (0,20) if number <10]
print(my_list)

# part 5 
conversion = 0.3048
my_depth_in_feet = [12.8, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(depth * conversion) for depth in my_depth_in_feet]
print (my_depth_in_meters)

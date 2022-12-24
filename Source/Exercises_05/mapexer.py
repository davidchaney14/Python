def double_number(n: int)->int:
    #Simple doubler
    return n+n
    
#Lsit of numbers
my_numbers = [1,2,3,4,5]
#Map my_numbers to the double_number function, return type is map?
result = map(double_number, my_numbers)
#Print a list of map
print(list(result))
#Iterate through it? 
for item in map(double_number, my_numbers):
    print(item)

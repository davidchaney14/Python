volume_of_cylinder = lambda radius, height : 3.142 * radius**2 * height
radius  = 5
height = 6
print(volume_of_cylinder(radius, height))

#Program to check if number has no remainder?
def divisible(numerator: int, denominator: int)-> bool :
    #Take value and divide and check if equal to 0 then use bool store
    return numerator % denominator == 0
#Output if numbers selected are equal to 0 IE nothing left over

print(divisible(30,4))

#print(divisible(30,5)) - > will return true

#Function to check number list for number provided outside of listed value and then provide bool if it is in it
def find_num(number_list: list, number: int)->bool:
    #Check number list for the number and iterate over it
    for iterate_number in number_list:
        #If found return true
        if iterate_number == number:
            return True
        #Return false instead of 'none' (remove the commented out code)
        #elif iterate_number != number:
        #    return False
        else:
            pass
#Number list
result = find_num([1,2,3,4,5,6,7,8], 9)
# result = find_num([1,2,3,4,5,6,7,8], 8) will result in True bool value
print(result)

#None due to it not being true but it is not false either!

#Function to search for even number
def find_num(number_list: list, number: int)->bool:
    #Check number list for the number and iterate over it
    for iterate_number in number_list:
        #If found return true
        if iterate_number % 2 == 0:
            return True
        #Return false instead of 'none'
        elif iterate_number != number:
            return False
        else:
            pass
#Number list
result = find_num([1,2,3,4,5,6,7,8], 9)
# result = find_num([1,2,3,4,5,6,7,8], 8) will result in True bool value
print(result)
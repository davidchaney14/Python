#Function to search for even number
def find_num(number_list: list, number: int)->bool:
    #Check number list for the number and iterate over it
    for iterate_number in number_list:
        #If found return true
        if iterate_number % number == 0:
            return True
        #Return false instead of 'none'
        #elif iterate_number % number != 0:
        #   return False
        else:
            False
#Number list
result = find_num([0,1,2,3,4,5,6,7,8],2)
print(result)
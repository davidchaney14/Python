# List test
my_list = [1,2,3,0]

for my_number in my_list:
    if my_number == 1:
        pass
    if my_number == 2:
        continue
    if my_number == 3:
        print(f"Found the number {my_number}")
    if my_number == 0:
        break

list_of_tuples =[(1,2),(3,4),("A","B")]
for item in list_of_tuples:
    print(item)

#Tuple unpacking
for a,b in list_of_tuples:
    print(a)
    print(b)

for index in range(1, 100, 5):
    print(index)

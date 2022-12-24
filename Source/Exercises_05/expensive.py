def most_expensive(price_list):

    #Iterate throught a list and find the most expensive items
    #Set up the variables
    max_price = 0
    max_price_item = ""
    #Unpack the tupple
    for description, price in price_list:
        # If max record it
        if price > max_price:
            max_price = price
            max_price_item = description
        # If not do nothing
        else:
            pass
    #Return back max price etc...
    return max_price_item, max_price
    
# Provide the data
price_list = [("Pineapple",1.0),("Apples",.5),("Pears",.7),("Peaches",.8)]
# Call function

# product, price, availability = most_expensive(price_list)
# C:\Users\admindc\OneDrive\0.ATU\0.IaC\Exercises_05>expensive.py
# Traceback (most recent call last):
# File "C:\Users\admindc\OneDrive\0.ATU\0.IaC\Exercises_05\expensive.py", line 22, in <module>
#    product, price, availability = most_expensive(price_list)
# ValueError: not enough values to unpack (expected 3, got 2)

product, price = most_expensive(price_list)
print(product,price)

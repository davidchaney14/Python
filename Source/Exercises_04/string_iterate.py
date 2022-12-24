#Define a string to iterate over
for this_letter in "David Chaney":
    #Specify which letter to test for
    if this_letter =="J":
        #Found test letter?
        print(f"Woo hoo, found a {this_letter}")
        #Exit check if not
        break
    else:
        #No letter found?
        print(f"Aww man, I didn't want a {this_letter}!")
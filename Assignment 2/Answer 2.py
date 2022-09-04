number = input("Enter a positive integer: ") #ask user to enter positive number

if number.isdigit(): # if loop to check 
    # int number
    number = int(number)
    #c) check if user entered number is positive or not
    if number > 0:
        #check if user entered number is even
        if number % 2 == 0:
            #printing statement if it is even
            print("You entered an even number")
        #if user entered odd number and is multiple of 7 
        elif number % 7 == 0:
            #printing
            print("You entered an odd number that is a multiple of 7")
        #else, if user entered odd and not multiple of 7
        else:
            print("You entered an odd number that is NOT a multiple of 7")
    #else, for negative number
    else:
        print("You did not enter a valid input!")
#for non digit 
else:
    print("You did not enter a valid input!")
    

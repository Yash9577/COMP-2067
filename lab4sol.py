                                                                    
myint = int(input("Enter a positive integer between 20 and 50: "))  # initialzied the variable myint and ask the user to enter number between 20 and 50 


if myint < 20:               # if the number entered by the user is less than 20 then this if loop will execute
    print(f"{myint} is less than minimum acceptable value.")


elif myint > 50:            # c. If the number entered by the user is greater than 50 then elseif loop will execute
    print(f"{myint} is higher than maximum acceptable value.")


else:           # If the user enters between the given numbers
    print(f"{myint} is within the acceptable range.")

    
    result = myint ** 3 / 7.351     # it will calculate the value of (myint) 3 / 7.351 and assign it to a variable result and print the value

    
    print("result = ", result)      # result will be printed

    
    result2 = int(result)       # the result will be converted into int and it will be assign to variable result2

    
    print("result2 = ", result2)    # result2 will be printed


print(f"The remainder obtained after diving {myint} by 5 = ", myint % 5)  # e. remainder will be calculated when myint is divided by 5 and it will print suitable message.

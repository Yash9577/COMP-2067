total = 0   # this variable stores the value of total and it is assigned to 0
while (True):# while in this program is being used to to check until the total comes to 100
    num = float(input("Please enter a number: ")) # this variable asks the user to enter the number for addition
    total += num # user inputed numbers are added to the variable total which is assigned to 0
    print(f"current total = {total}") # this print command prints the total value as it reaches the total of 100
    if (total > 100): # this if loop is used to check that as the total reaches 100 the while loop is breaked and the value is printed
        break

x = total**2   # this command calculates the square of total
print(f"total = {total}")  # total is printed through this print staatement
print(f"The square of {total} is {round(x, 1)}") # this print statement prints the square total

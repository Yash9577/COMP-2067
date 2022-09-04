fibonacci = [] #this variable stores the value of fibonacci numbers
x = 0 # first variable of fibonacci numbers
y = 1 # second variable of fibonacci numbers

for i in range(20): # for loop is used to get the range of fibonacci numbers
    
    fibonacci.append(x) #using append command for the first element
    # this is the logic to get the fibonacci sequence
    z = x+y
    x = y
    y = z

print("The first 20 Fibonacci numbers are: {}".format(fibonacci)) #this print statement prints the first 20 fibonacci numbers in sequence

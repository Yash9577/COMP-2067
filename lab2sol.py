x=3 # variable x with assigned value
print("x = ", x) # printing value to variable x with suitable message

print("After converting to float", float(x)) # converted x variable to float 

y=-9.677 # variable y with assigned value
print("y = ", y) # printing the value to variable y with suitable message

z=y**x # calcualting expression with assigned variable to z
print("The value of y**x is: z = ", z) # printing variable z with suitable message

print("The value of z rounded to 3 decimal places =", "{:.3f}".format(z)) # rounded z to 3 decimal places 

print("The absolute value of z is:",abs(z)) # displayed absolute value of z variable

result=(x*y+7)/(x+y) # calculating the expression 


print(round(result)," is the rounded up value of result") #assigning the answer to variable result

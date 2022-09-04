x = int(input("Enter integer between 0 and 8:")) #ask user to input integer between 0 and 8
i = 1

while x <= 50: #while loop x is less than to then the following loop will execute
 print("x = ",x)
 
 if (x % 9 == 0): #if x is multiple of 9 then print the following statement
  print("found multiple of 9")
  break
  
 else: # then update x by adding 10 to the current value
    x = x+10
    i = i+1
 
print("The final value of x is ",x) #printing the final value
print("The loop was entered ",i," times") #printing the number of loops it was entered

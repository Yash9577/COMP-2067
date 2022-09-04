#A
list1 = ['windsor', 'toronto', 'ottawa', 'montreal', 'vancouver'] # initializing variable list1
print("list1 = ",list1) #printing list1

#B
print("The last 3 characters of the first element of list1 are:",list1[0][4:]) #printing last 3 characters of first element of list1

#C
cityname = input("Enter the name of a city in lowercase: ") #asking user to enter city name in lowercase
print("cityname = ", cityname.upper()) # printing cityname in uppercase letters

#D
list1.append("waterloo") # adding the cityname at the end of list1
print("The updated list1 after appending item is: ",list1) # printing the updated value of list1

#E
minimumValue=min(list1) 
replace=list1[(list1.index(min(list1)))]='minval' 
print("The updated list1 after replacing item is: ",list1) #printing the updated list1 after replacing using append



#F
birthyear=int(input("Enter your year of birth (yyyy):")) # initializing birthyear variable that user can enter
print("year =",birthyear) #printing birth year entered by user

#G
Lenght=len(list1) 
print("Number of elements in list1:",Lenght) # printing number of elements in list1
sum= birthyear + Lenght # adding birthyear to updated list1
print("sum =",sum) #printing sum of birthyear and list1

list1 = [4, 2, 7];  # initializing variable list1
list2 = [3, 1, 9, 2]; # initializing variable list2
prod_list= []
print(f"list1 = {list1} ; list2 = {list2}") # printing list1 and list2

def multiply_lists(list1, list2): #defining function multiply_lists
    temp_list = [] 
    for ele1 in list1: #for loop
        for ele2 in list2:
            prod_list.append(ele1*ele2) # using append command to multiply ele1 and ele2
    return prod_list # returning prod_list 


prod_list = multiply_lists(list1, list2) #initializing variable prod_list and calling the function multiply_lists

print(f"prod_List = {prod_list}") #printing the multiplication of list1 and list2 initialised in 

print(f"sum = {sum(prod_list)}.") # printing the sum of prod_List

print(f"Number of occurrences of 4 is: {prod_list.count(4)}") #printing number of 4 occured in prod_List

print(f"72 is in prod_list: {72 in prod_list}") #printing true or false if 72 is in the list

prod_list.sort() # using sort function to sort prod_List
print(f"sorted list = {prod_list}") #printing sorted list

x = ['A','E','I','O','U','a','e','i','o','u'] # initializing vowels to variable
name = input("Enter your name: ") # asking user to enter name
if name[0] in x: # first character of name input by user is vowel then it will print the below statement
    print("Your name starts with a vowel.")
else: # first character of name input by user is constant then it will print the below statement
    print("Your name starts with a consonant.")
# printing the first character in upper case
print(f'The first letter of your name is: {(name[0]).upper()}')


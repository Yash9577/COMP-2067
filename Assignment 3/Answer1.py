wordList=['hat','book','house','flower','tree','grass','cheetah','lion','tiger','car','boat']# this variable contains 10 strings that are used to check if their spelling contains vowels or not

for i in range(0,len(wordList),3): # this for loop will run from 0 to the number of strings given in the variable wordlist
  vowel=0
  # iterate through string at i
  for char in wordList[i]:
    # if char is vowel, increment vowel
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U': # if a vowel is found in char than the vowel is increased by 1
      vowel=vowel+1
  print(wordList[i],"contains",vowel,"vowel(s)")

  if vowel>=3: # The string contains more than 3 vowels than the loop will break and print the following statement
    print("***Found string with 3 or more vowels!***")
    break
else: # if it does not break the loop it will execute this else loop and print the given statement
  print("***Did not find suitable string.***")

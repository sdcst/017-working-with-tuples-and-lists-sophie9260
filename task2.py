#!python3

"""
Create a variable that contains an empty list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
newList = []
w1 = input("Enter a word => ")
w2 = input("Enter a word => ")
w3 = input("Enter a word => ")
w4 = input("Enter a word => ")
w5 = input("Enter a word => ")

newList.append(w1)
newList.append(w2)
newList.append(w3)
newList.append(w4)
newList.append(w5)

print(newList)

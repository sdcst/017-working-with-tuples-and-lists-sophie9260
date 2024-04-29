#! python3
"""
Print the list named "fruit".
Ask the user to enter a word
If the word is in the list, delete all occurrences of that word from the list
If the word is not in the list, add the word to the list
Print out the updated list

inputs:
string

outputs:
list

examples:
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:kiwi
['apple', 'cherry', 'apple', 'banana', 'strawberry', 'blueberry']

['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:orange
word not in list
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi', 'orange']

"""

fruit = ["apple","cherry","kiwi","apple","banana","strawberry","kiwi","blueberry","kiwi"]
print(fruit) 

word = input("Enter a word => ")
word = str(word)

x = fruit.count(word)

if x <= 0:
    print(f"The word entered is : {word}. but it isn't in the list, so it will be added. ")
    fruit.append(word)
    print(fruit)
if x > 0:
    x = x + 1
    for i in range(1, x):
        fruit.remove(word)
    else:
        print(f"The word entered is : {word}. and it will be removed from the list.")
        print(fruit)



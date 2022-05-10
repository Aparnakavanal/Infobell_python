#print odd an even numbers in a list

num = 1,3,5,66,3,2,8,9,11 #a variable which contains numbers
odd = [] #an empty list to store odd numbers
even = [] #an empty list to store even numbers

for i in num: #iterating the numbers
    if i%2 == 0: #checking the condition if the num is even
        even.append(i) #if the condition satisfied then append it to the list named even
    else:
        odd.append(i) #if else condition satisfied then append the numbers in to the list named odd
print(even,"even numbers")
print(odd,"odd numbers")
#find the count of repeating numbers in the list

lst = [1,2,3,4,5,6,6,7,7,8,8,9,1,2] #a list with some numbers
co = [] #an empty list
for i in lst: #iterating the lst
    if i not in co: #checking if the numbers is not in the list co
        co.append(i) #if condition satisfied then append it to the list co
        print(i,"is repeated",lst.count(i),"times")
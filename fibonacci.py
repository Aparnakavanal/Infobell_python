# print fibonacciseries

# num1 = 0
# num2 = 1
# for i in range(10):
#     print(num1)
#     total = num1 + num2
#     num1 = num2
#     num2 = total


def fibanaci(n):
    # initilizing first term
    num1 = 0
    # initilizing second term
    num2 = 1
    # checking conditions, because fibonacciseries accepts only positive numbers
    if n >= 0:
        # iterating the n
        for i in range(n):
            # printing the first term
            print(num1)
            # adding fist and second term
            total = num1 + num2
            # assigning num2 in nto num1
            num1 = num2
            # assigning total to the num2
            num2 = total
    else:
        print("give positive numbers only!")
# giving a value to n
fibanaci(20)





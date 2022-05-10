#printing a prime numbers

def prime(n): #defining a function
    if n>1: #checking if n is greater than 1
        for i in range(2,n): #iterating through 2 and n to check for factors
            if i%n ==0: #if n is divisible by any number between 2 and n then it is not prime
                print(n,"is not prime")
                break #when condition satisfied then break the loop
        else:
            print(n,"is prime")
    else:
        print(n,"is not prime") #it will show if the num is not prime

prime(2) #calling the function
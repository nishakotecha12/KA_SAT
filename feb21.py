"""
1. create a function to check whether a number is prime or not

num = int(input("Enter a number: "))
# range has 3 parameters : start, stop, step
for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")

#2. write a program to print a list of prime numbers between 1 and 500

prime=[]
for num in range(2, 501):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime.append(num)
print(prime)


#3 . write a dynamic user input program to print prime numbers between 1 and n
n = int(input("Enter a number: "))
prime=[]
for num in range(2, n+1):
    for i in range(2, num):
        if num % i == 0:
            break
                
    else:
        prime.append(num)
print(prime)
 

#4 . write a dynamic user input program to print prime numbers between n and n
n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
prime=[]
for num in range(n, m+1):
    for i in range(2, num):
        if num % i == 0:
            break
                
    else:
        prime.append(num)
print(prime)

#5.write a program to check if a number is armstrong or not
num = int(input("Enter a number: "))
snum = str(num)
n = len(snum)
s = 0
for i in snum:
    s = s + int(i)**n
if s == num:
        print(True)
else:
        print(False)
        

#6 WAP TO PRINT LIST OF ARMSTRONG NUMBERS BETWEEN GIVEN RANGE
n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
armstrong = []
for num in range(n, m+1):
    snum = str(num)
    n = len(snum)
    s = 0
    for i in snum:
        s = s + int(i)**n
    if s == num:
        armstrong.append(num)
        
print(armstrong)
        
"""    

    
            
 

   
    


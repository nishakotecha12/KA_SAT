#write a program to count how many vowels(a,e,i,o,u) are there in a given string    
#def count_vowels(S):
#    count=0
#    for i in S:
#       if i in 'aeiouAEIOU':
#            count+=1
#    return count
#S=input("Enter a string: ")
#print("Number of vowels in the string is: ",count_vowels(S))

#name="NISHA"
#count=0
#for char in name:
#    if char in 'AEIOU':
#       count+=1
#        print(count)

#Write a program to reverse a string using a loop(without using slicing[::-1])
#def reverse_string(S):
#    reversed_str=""    
#    for char in S:
#        reversed_str=char+reversed_str
#    return reversed_str
#S=input("Enter a string: ")
#print("Reversed string is: ",reverse_string(S))

#students=["kunal","Rahul","pawan","arjun"]
#Write a program to print the names of students in reverse order without using slicing[::-1] in a different list also do reverese of each string
#reversed_students=[]
#for student in students:
#    reversed_name=""
#    for char in student:
#        reversed_name=char+reversed_name
#    reversed_students.append(reversed_name)
#print("Reversed names of students: ",reversed_students)

#rev_name=[]
#for name in students:
#    rev=""
#    for char in name:
#        rev=char+rev
#        rev_name.append(rev)
#    print(rev_name)

#write a program to count how many even numbers and how many odd numbers are there in a list of numbers (use logic of count)

#numbers=[10,22,34,32,46,78,67,57,98,33]
#even=0
#odd=0
#for num in numbers:
#    if num%2==0:
#        even+=1
#    else:
#        odd+=1
#print("Number of even numbers: ",even)
#print("Number of odd numbers: ",odd)

#numbers=[10,22,34,32,46,78,67,57,98,33]
#even_count=0
#odd_count=0
#for num in numbers:
#    if num%2==0:
#        even_count=even_count+1
#    else:
#        odd_count=odd_count+1
#print(even_count)
#print(odd_count)


#write a pg to check if a given string is palindrome or not using loops
#string = "KUNALANUK"
#rev_str=""
#for char in string:
#    rev_str=char+rev_str
#if string==rev_str:
#   print("The string is a palindrome.")
#else:
#    print("The string is not a palindrome.")
    
#write a pg to check if a given string is palindrome or not using functional programming
#def is_palindrome(s):
#    rev_str=""
#    for char in s:
#        rev_str=char+rev_str
#    return s==rev_str
#string = input("Enter a string: ")
#if is_palindrome(string):
#    print("The string is a palindrome.")
#else:    print("The string is not a palindrome.")

#write a pg to find the frequency of each character in a given string using a dictionary
#name="mississippi"
#freq={}
#for char in name:
#   if char in freq:
#        freq[char]+=1
#    else:
#       freq[char]=1
#print("Frequency of each character: ",freq)

#create a function to calculate addition of 2 numbers
#def add_num(a=0,b=0):
#    return a+b
#num1=float(input("Enter first number: "))
#num2=float(input("Enter second number: "))
#result=add_num(num1,num2)
#print("The sum of the two numbers is: ",result)

#(in general code that goes for all the quesries and errors )
#def sum(a=0,b=0):
#    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
#        return a+b
#    else:
#        return "Invalid input. Please enter numbers."
#def get_number(prompt):
#    while True:
#        val = input(prompt)
#        try:
#            return float(val)
#        except ValueError:
#            print("Invalid input. Please enter a number (int or float).")

#num1 = get_number("Enter first number: ")
#num2 = get_number("Enter second number: ")
#result = sum(num1, num2)
#print("The sum of the two numbers is: ", result)

#OR

#def sum(a=0,b=0):
#    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
#       result= a+b
#        return result
#    else:
#        print("Invalid input. Please enter numbers.")
#        n1=eval(input("n1: "))
#        n2=eval(input("n2: "))
#        return sum(n1,n2)
#        return result
#    print(sum())

#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------

#write a function to return square of a number

#def square(num):
#   return num**2
#number=float(input("Enter a number: "))
#result=square(number)
#print("The square of the number is: ",result)

#def getSquare(n):
#    return n ** 2

#num = int(input("Enter a number: "))
#print("Square of the number is:", getSquare(num))

#write a function to return cube of a number

#def cube(num):
#    return num**3  
#number=float(input("Enter a number: "))
#result=cube(number)
#print("The cube of the number is: ",result)


#def getCube(n):
#    return n ** 3

#num = int(input("Enter a number: "))
#print("Cubeof the number is:", getCube(num))

#write a function to return power of a number
#def power(base,exp):
#    return base**exp
#base=float(input("Enter the base number: "))
#exp=float(input("Enter the exponent: "))
#result=power(base,exp)
#print(f"{base} raised to the power of {exp} is: ",result)

# Take input
#base = float(input("Enter the base number: "))
#exp = int(input("Enter the exponent (integer): "))

# Using Python's built-in power operator
#def power(base, exp):
#    return base ** exp

# Using loop to calculate power manually
#def getPower(base, exp):
#    p = 1
#    for i in range(1, exp + 1):
#        p = p * base
#    return p

# Example run
#print("Using ** operator:", power(base, exp))
#print("Using loop:", getPower(base, exp))

#write a function to return count of number which is divisible by 4 and 7 in range -123 to 233
#def count_divisible(start, end):
#    count = 0
#    for num in range(start, end + 1):      
#        if num % 4 == 0 and num % 7 == 0:
#            count += 1
#    return count
#start = -123
#end = 233
#result = count_divisible(start, end)
#print(f"Count of numbers divisible by 4 and 7 in range {start} to {end} is: ", result)

#write a function to check the given number is prime or not
#def isPrime(num):
#    if num > 1:
#        for i in range(2, num):
#            if num % i == 0:
#                return False   # not prime
#        return True            # prime
#    else:
#        return False           # 1 or less are not prime

# take input
#n = int(input("Enter a number: "))

# call the function
#if isPrime(n):
#    print(n, "is a prime number.")
#else:
#    print(n, "is not a prime number.")


#def check_prime(num):
#    count = 0
#    for i in range(1, num + 1):
#        if num % i == 0:
#            count += 1
#    if count == 2:
#        print("prime number")
#        
#    else:
#        print("not a prime number")
        
#number = int(input("Enter a number: "))
#check_prime(number)

#write a function to print prime numbers from 1 to 100
#def printPrimes(n):
#    for num in range(1, n + 1):
#        count = 0
#        for i in range(1, num + 1):
#            if num % i == 0:
#                count += 1
#        if count == 2:
#            print(num, end=" ")
#
#n = 100
#printPrimes(n)

#def print_primes(n1,n2):
#    for i in range(n1,n2+1):
#        if(checkprimeNumber(i)==True):
#            print(i)
            

#write a function to print count of prime numbers from 1 to 100 using functional programming using above Code
#def is_prime(num):
#    if num > 1:
#       for i in range(2, num):
#            if num % i == 0:
#                return False   # not prime
#        return True            # prime
#    else:
#        return False           # 1 or less are not prime


#def count_primes(n):
#    count = 0
#    for i in range(1, n + 1):
#        if is_prime(i):
#            count += 1
#    return count


# main code
#n = 100
#print("Total prime numbers from 1 to", n, "are:", count_primes(n))

#write a function to print divisors of a given number

#def print_divisors(num): 
#    print("Divisors of", num, "are: ", end="")
#    for i in range(1, num + 1):
#        if num % i == 0:
#            print(i, end=" ")

#number = int(input("Enter a number: "))
#print_divisors(number)
    
#write a function to print count of divisors of a given number
#def count_divisors(num):
#    count = 0
#    for i in range(1, num + 1):
#        if num % i == 0:
#            count += 1
#    return count

#number = int(input("Enter a number: "))
#result = count_divisors(number)
#print(f"Count of divisors of {number} is: {result}")

#write a function to print sum of divisors of a given number
#def sum_divisors(num):
#    total = 0
#    for i in range(1, num + 1):        
#        if num % i == 0:
#            total += i
#    return total

#number = int(input("Enter a number: "))
#result = sum_divisors(number)
#print(f"Sum of divisors of {number} is: {result}")


#def sum_divisors(num):
#    total = 0
#    for i in range(1, num):        
#        if num % i == 0:
#            total += i
#    return total

#number = int(input("Enter a number: "))
#result = sum_divisors(number)
#print(f"Sum of divisors of {number} is: {result}")

#write a function to check if a given number is perfect number or not
#def is_perfect(num):
#    total = 0
#    for i in range(1, num):
#        if num % i == 0:
#            total += i
#    return total == num

# Example usage:
#number = int(input("Enter a number: "))
#if is_perfect(number):
#    print(f"{number} is a perfect number.")
#else:
#    print(f"{number} is not a perfect number.")

#write a function to print perfect numbers from 1 to 100

#def perfect():
#    for n in range(1, 101):
#        s = 0
#        for i in range(1, n):
#            if n % i == 0:
#                s = s + i
#        if s == n:
#            print(n)
#
#perfect()
      

        
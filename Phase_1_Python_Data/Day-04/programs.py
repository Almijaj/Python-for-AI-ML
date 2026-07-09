# practice problems
# 1.Function to add two numbers.

def sum_add(a,b):
    addition=a+b
    print(addition)

sum_add(3,4)

# # 2.Function to subtract two numbers.

def sum_sub(a,b):
    subtraction=a-b
    print(subtraction)

sum_sub(9,6)

# # 3.Function to multiply two numbers.

def sum_multiply(a,b):
    multiplication=a*b
    print(multiplication)

a=3
b=4
sum_multiply(a,b)

# # 4.Function to divide two numbers.
def sum_Div(a,b):
    division=a/b
    print(division)

a=12
b=4
sum_Div(a,b)

# # 5.Function to find the square of a number.

def square(a):
    suq=a*a
    print(suq)

a=int(input("enter the number="))
square(a)

# 6.Function to check even or odd.

def check(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
    

a=int(input("enter the number"))
check(a)

# # 7.Function to find the largest of three numbers.

def largest(a,b,c):
    if(a>b and a>c):
        print("a is greatest")
    elif(b>a and b>c):
        print("b is the greatest")
    else:
        print("c is the greatest")

a=5
b=9
c=10
largest(a,b,c)

# 8.Function to calculate factorial.

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number: "))
answer = factorial(num)

print("Factorial =", answer)

# 9.Function to calculate the sum of first n numbers.

def sum_n_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


num = int(input("Enter a number: "))

answer = sum_n_numbers(num)

print("Sum =", answer)

# 10.Prime number using a function.

def num_is_prime(num):
    for i in range(2,num):
        if (num%i==0):
            print("'number is not a prime number")
            break
        else:
            print("number is a prime number")
            break

num=int(input("enter the number"))
num_is_prime(num)
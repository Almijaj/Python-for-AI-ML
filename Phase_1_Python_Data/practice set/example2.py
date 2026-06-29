# program 1
# i=0
# for i in range(100):
#    print(i+1)
#    program 2
# for i in range(1,101):
#     if(i%2==0):
#         print(i)
# program 3
# num = int(input("Enter number: "))

# for i in range(1, 11):
#  print(num,"X",i,"=",num*(i))
# program 4
# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i

# print(sum)
# program 5
# n=int(input("enter the number"))
# factorial=1
# for i in range(1,n+1):
#  factorial=factorial*i
# print(factorial)
# program 6
n = int(input("Enter a number: "))

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")
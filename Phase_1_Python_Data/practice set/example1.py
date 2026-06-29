# # program 1
num=int(input("enter the num:"))
if(num%2==0):
    print("its even")
else:
    print("its odd")

# # program 2
age=int(input("enter your age ="))
if(age>=18):
    print("person can vote")
else:
    print("cant vote")

# # program 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
elif(c>a and c>b):
    print("c is greater")


# # program 4
num1=int(input("enter the num1="))
if(num1>0):
    print("its positive")
elif(num1<0):
    print("its negative")
else:
    print("its zero")

# # program 5
grade=int(input("enter the value"))
if(grade>=90):
    print("A")
elif(grade<=89 and grade>=79):
    print("B")
elif(grade<=74 and grade>=60):
    print("C")
else:
    print("fail")

# program 6
firstnum=int(input("enter value"))
operator=input("enter the sign")
secnum=int(input("enetr value again"))
if(operator=="+"):
    print(firstnum+secnum)
elif(operator=="-"):
    print(firstnum-secnum)
elif(operator=="%"):
    print(firstnum%secnum)
elif(operator=="*"):
    print(firstnum*secnum)
elif(operator=="/"):
    print(firstnum/secnum)
else:
    print("invalid")

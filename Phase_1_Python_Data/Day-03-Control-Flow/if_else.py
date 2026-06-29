# if-else statements = its basically to check the conditions
 # conditional operator
# >,<,<=,>=,==,!=
a=int(input("enter your age"))
print("your age is ",a)
# print(a<18)
# print(a<=18)
# print(a>=8)
# print(a==18)
# print(a!=18)
if(a>18):
    print("you can drive ")
else:
    print("you cannot drive")

# the space you see here is called indentation
# program 1
num=int(input("enter your number"))
if(num<0):
    print("number is negative")
elif (num==0):
    print("number is zero")
else:
    print("number is positive")
# nested program
num1=int(input("enter the number1:"))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")
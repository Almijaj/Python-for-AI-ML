# Program 1-Take your name as input and print:
# a=input("enter your name:")
# print("hello",a)
# Program 2-Take two numbers and print:
# a=int(input("enter the number1"))
# b=int(input("enter the number2"))
# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# print(add,sub,mul,div)
# Program 3-Take age as input and print:
# age=input("enter your age")
# print("my age is ",age)
# print(type(age))
# Program 4-Convert Celsius to Fahrenheit.
# c=float(input("enter the value"))
# f=(c*9/5)+32
# print(f)
# Program 5-Convert Fahrenheit to Celsius.
#  f=float(input("enter the value"))
# c=(f-32)*5/9
# print(c)
# Program 6-Swap two numbers using a temporary variable.
# a=10
# b=20
# c=10
# b=a
# a=20
# print(a,b)
# Program 7-Swap two numbers without a temporary variable.
# a=3
# b=5
# a,b=b,a
# print(a,b)
# Program 9-Calculate the area of a rectangle
# lenght=int(input("enter the value"))
# breadth=int(input("enter the value"))
# area=lenght*breadth
# print(area)
# Program 9-Calculate the area of a circle.
# radius=int(input("enter the number"))
# area=3.14*radius*radius
# print(area)
# Program 10-Build a simple marks calculator.
totalmax=500
maths=int(input("enter the maths marks"))
science=int(input("enter the science marks"))
history=int(input("enter the history marks"))
geography=int(input("enter the geography marks"))
english=int(input("enter the english marks"))
totalgained=maths+science+history+geography+english
percentage=(totalgained/totalmax)*100
print(totalgained)
print(percentage)
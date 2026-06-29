# Program 1-Even or Odd
# a=int(input("enter the number"))
# if(a%2==0):
#     print("its even")
# else:
#     print("its odd")
# Program 2-Voting Eligibility
# age=int(input("enter the value="))
# if(age>=18):
#     print("person can vote")
# else:
#     print("person can't vote")
# Program 3-Largest of Three Numbers
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if(a>b and a>c):
#     print("a is grater")
# elif(b>a and b>c):
#     print("b is greater")
# elif(c>a and c>b):
#     print("c is greater")
# Program 4-Positive, Negative or Zero
# a=int(input("enter the value"))
# if(a>0):
#     print("positive")
# elif(a<0):
#     print("negative")
# elif(a==0):
#     print("zero")
# Program 5-Grade Calculator
# marks=int(input("enter the value"))
# if(marks>=90):
#     print("A+")
# elif(marks<=90 and marks>=85):
#     print("A")
# elif(marks<=85 and marks>=65):
#     print("B")
# elif(marks<=65):
#     print("C")
# Program 6-Calculator using if-elif-else
# a=int(input("enter the value: "))
# b=int(input("enter the value: "))
# operator=input("enter (+,-,*,/,%): ")

# if (operator=="+"):
#     print(a+b)
# elif(operator=="-"):
#     print(a-b)
# elif(operator=="*"):
#     print(a*b)
# elif(operator=="/"):
#     print(a/b)
# elif(operator=="%"):
#     print(a%b)
# Program 7-BMI Calculator
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))

# bmi = weight / (height ** 2)


# if bmi < 18.5:
#     print("Category: Underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("Category: Normal")
# elif bmi >= 25 and bmi < 30:
#     print("Category: Overweight")
# else:
#     print("Category: Obese")
# Problem 1-
# num=int(input("enter the number"))
# if(num%5==0):
#     print("buzz")
# elif(num%3==0):
#     print("fizz")
# else:
#     print("fizzbuzz")
# Problem 2-Find the greatest among four numbers.
first_num=int(input("enter first num"))
second_num=int(input("enter second num"))
third_num=int(input("enter third num"))
fourth_num=int(input("enter fourth num"))
if (first_num>second_num and first_num>third_num and first_num>fourth_num):
    print("first num is greater")
elif(second_num>first_num and second_num>third_num and second_num>fourth_num):
    print("second num is greater ")
elif(third_num>first_num and third_num>second_num and third_num>fourth_num):
    print("third num is greater ")
elif(fourth_num>first_num and fourth_num>second_num and fourth_num>third_num):
    print("fourth num is greater")
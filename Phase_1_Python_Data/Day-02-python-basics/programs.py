# Level 1
# 1.Find the length of a string.
str="Almijaj"
print(len("almijaj"))
# 2.Convert to uppercase.
print(str.upper())
# 3.convert to the lowercase
print(str.lower())
# 4.Reverse a string.
str=input("enter the string:")
reverse=""
for i in range(len(str)-1,-1,-1):
    reverse=reverse+str[i]
print("reversed string",reverse)
# 5.count vowels
str=input("enter the string=")
count=0
for ch in str:
  if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
     count=count+1
print("number of vowels",count)  
# 6.count consonents
str=input("enter the string=")
count=0
for ch in str:
    if ch.isalpha():
     if ch not in "aeiou":
       count=count+1
print("number of consonents",count)      
# 7.count words
str=input("enter a string=")
count=1
for ch in str:
   if ch==" ":
      count=count+1
print("number of words",count)
# 8.remove spaces
str=input("enter the string=")
result=""
for ch in str:
   if ch!=" ":
      result=result+ch
print("removing spaces",result)
# 9.check palindrome
str=input("enter the string:")
reverse=""
for i in range(len(str)-1,-1,-1):
    reverse=reverse+str[i]
if(str==reverse):
    print("its palindrome")
else:
    print("its not palindrome")
# 10.Count uppercase and lowercase letters.
string = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in string:
    if ch.isupper():
        uppercase = uppercase + 1
    elif ch.islower():
        lowercase = lowercase + 1

print("Uppercase letters =", uppercase)
print("Lowercase letters =", lowercase)
# 11.Count digits in a string.
str=input("enter the string=")
count=0
for ch in str:
   if ch.isdigit():
      count=count+1
print("the number of digits are",count)
# 12.Count special characters.
str=input("enter the string")
count=0
for ch in str:
   if not ch.isalpha() and not ch.isdigit():
      count=count+1
print("number of special character",count)
# 13.Find the first non-repeating character.
string = input("Enter a string: ")

for ch in string:
    count = 0

    for x in string:
        if ch == x:
            count = count + 1

    if count == 1:
        print("First non-repeating character:", ch)
        break
# 14.Check if two strings are anagrams.
string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not an Anagram")
      
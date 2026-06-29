# string methods 
a="harry? ?? ???"
print(len(a))
# strings are immutable 
# for  converting string into upper string 
print(a.upper())
# for converting string into lower string 
print(a.lower())
# rstrip () removes any trailing character  ye sirf characters ke baad jo lage trailing ko hata ta hai starting walo ko nhi
print(a.rstrip("?"))
# replace() so basically we can change entire string all occurance jha jha ye word present hoga 
print(a.replace("harry","almijaj"))
# split() this converts string into list 
print(a.split(" "))
# capitalize() basically this capitalize the first letter and rest of the character into lower ccase 
blogheading="introduction to python"
print(blogheading.capitalize())
# centre() so basically this adds the spaces to make the character be in centre/middle 
str1="welcome to the codes series !!!"
print(len(str1))
print(len(str1.center(50)))
# count() ye actually count krta hai ek character mai kitne letters repeat hue hai 
print(a.count("harry"))
str1="welcome to the ad vibe!!!"
print(str1.endswith("!!!"))
# here it checks weather the given value ends in given comdition
str2="welcome to the console!!! "
print(str2.endswith("to",4,10))
# find() it finds letter in the string and tell the position
str2="my name is almijaj . i am a honest man"
# this dosent give any error
print(str2.find("ishh"))
# this gives error 
# print(str2.index("ishh"))
# isalnum() this is method returns true only if entire string consist A-Z,a-z,0-9
str3="WelcomeToTheConsole "
print(str3.isalnum())
# this checks wheater there are only character or number 
str3="welcome"
print(str3.isalpha())
# islower() so this checks all the characters are lower 
str4="google"
print(str4.islower())
# isprintable()  if the values  within the given string are printable if they not return false 
str4="we wish you marry christmas "
print(str4.isprintable())
# isspace()  true only when it contains white space 
str4="             "
print(str4.isspace())
# istitle() only returns true if the first letter is capitalize 
str5="World Health Organization"
print(str5.istitle())
# startswith() it checks the given character starts with 
str6="python is object oriented program"
print(str6.startswith("python"))
# swapcase() it converts upper case to lower case and lower case to upper case 
str6="python is object oriented program"
print(str6.swapcase())
# title() it capitalize each letter of the word the string 
str6="he is dan,he is good person"
print(str6.title())
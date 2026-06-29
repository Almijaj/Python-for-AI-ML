# strings = anything we write in single or double quation is consider as string 
# example=a="almijaj"  and a='almijaj'
print('he said , "i want to eat an apple .')
# for multiple  strings we can use triple single quatation or triple double quatation 
a=""" we are players 
so thought u are the "dreamer "
we are a dreamer we can go through world making changes """
print(a)
b='''dil pe zkhm khate hai , "jaan se guzarte hai"
dil pe zakhm khate hai ,"jaan se guzarte hai" 
zurm sirf itna hai tumko pyar krte hai '''
print(b)
# accesing character of string 
# print="hello " here hello is sequence of character which has value for ex= h=0 ,e=1,l=2,l=3,o=4
name="wassup"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


# in python string is like an array of character , array is collection of items 
# looping through strings basically this is used when we have paragraph  
print("lets use for loop\n")
for character in b :
    print(character)
    # this is like a blakbox jo ek ek krke sare string print krta hai 
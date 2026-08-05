# while loop this are used in complex conditions
# it excecutes the program as the condition is true otherwise it gives error 
i=0
while(i<=3):
 print(i)
 i=i+1

k=int(input("enter your number"))
while(k<=32):
 k=int(input("enter your number"))
 print(k)


#  decrementing while loop
count=5
while(count>0):
 print(count)
 count=count-1 
else:
 print("i am inside else ")

# while loop with else
i=0
while i<7:
 print(i)
 i=i+1
 if i==4:  #basically this doesnot print the else statement
  break

else:
   print("sorry no i")

# example
for x in range(5):
 print("iteration no{} in for loop".format(x+1))
else:
 print("else block in loop")
print("out of loop")
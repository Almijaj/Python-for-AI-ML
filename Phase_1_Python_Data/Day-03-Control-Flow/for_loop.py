# loops-sometimes programer wants to exceute group of statements a certain number of times 
# for loop=can iterate over sequence iterable objects in python 
name='almijaj'
for i in name:
    print(i)
    if(i=="m"):
        print("there is something special")
    # so basically here there is string so the for loop prints each letter iterate 

#niw there is another example of list
colors=["Red","green","Blue","yellow"]
for color in colors:
    print(color) 
    for i in color:
        print(i)
# for range-range(1,200)
for k in range(20):
    print(k+1)

for k in range(1,12,2):
    print(k)
# for loop with else
for i in range (5):
    print(i)
else:                      #the statements in the else block will be executed after all iteration are completed 
    print("sorry no i")

#for loop withe else (with condition)
for i in range(6):
    print(i)
    if i==4:
        break
else:
        print("sorry no i")

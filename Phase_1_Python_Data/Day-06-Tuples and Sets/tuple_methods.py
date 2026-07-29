# manipulating tuples : Tuples are immutable hence if you want to add,remove or change tuple items,then first you must convert
# the tuple to list .Then perform operation on that list and convert it back to tuple
# example 1
countries=("spain","Itlay","India","England","germany")
temp=list(countries)
temp.append("russia")  #add item
temp.pop(3)                #remove item
temp[2]="Finland"       #change item
countries=tuple(temp)
print(countries)
# concatenate two tuple
countries1=("pakistan","afgahanistan","bangladesh","srilanka")
countries2=("vietnam","india","china")
southeastasia=countries1+countries2
print(southeastasia)
# tuple methods
# count() method
tuple=(0,1,2,3,2,3,1,3,2,3)
res=tuple.count(3)
print("count of 3 in tuple is :",res)
# index() method : returns first occurances of given element in the tuple from the tuple
tuple=(0,1,2,3,2,3,1,3,2,3)
res=tuple.index(3)
res=tuple.index(3,4,8)
print("first occurance of the 3 is:",res)
print(len(tuple))
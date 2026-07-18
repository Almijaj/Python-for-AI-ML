# List methods
# list.sort()=this method is used to arrange the data sequencly in asccending order
L=[32,54,4,5,6,7,8]
L.sort()
print(L)
# list.sort(reverse=true)print data in descending order
l=[34,65,44,65,7,8,9,90]
l.sort(reverse=True)
print(l)
# reverse() basically here it reverse the list 
l=[32,54,67,87,3,2,4]
l.reverse()
print(l)
# append() basically this is used to add the element in the list at last
l=[43,65,4,5,7,84]
l.append(4)
print(l)
# index() this method returns the index of the first occurance of the list item
colours=["violet","green","indigo","blue","green"]
print(colours.index("green"))
print(colours.index("violet"))
print(colours.index("indigo"))
print(colours.index("blue"))
# count() we can count the number of items with the given value
colours=["violet","green","indigo","blue","green"]
print(colours.count("green"))
# copy() returns copy of the list this can be done to perform operations on the list without modifying the original list
colours=["violet","green","indigo","blue"]
newlist=colours.copy()
print(newlist)
# insert() this method insert an item at the given index.user has to specify index and the item to be inserted with the insert() method
colours=["violet","indigo","blue"]
colours.insert(1,"green")
print(colours)
# extend() this basically extends the list to the first list
colours=["violet","indigo","blue"]
rainbow=["green","yellow","orange","red"]
colours.extend(rainbow)
print(colours)
# concatenating two list
colours1=["violet","indigo","blue","green"]
colours2=["yellow","orange","red"]
print(colours1+colours2)
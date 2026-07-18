# basic introduction
# example 1
list1=[1,2,3,4,5,6]
list2=["red","green","blue"]
print(list1)
print(list2)
# example 2
details=["abhijeet",18,"FYBScIT",9.8]
print(details)
# list index 
colours=["red","green","blue","black","yellow"]
            #   0      1          2         3          4       (positive indexing)
            #   -5    -4        -3         -2         -1      (negative indexing)
# accesing positive list index  
print(colours[0])
print(colours[1])
print(colours[2])
print(colours[3])
print(colours[4])
# accesing negative list index
# we can calculate it by len(marks)-any number
print(colours[-1])
print(colours[-2])
print(colours[-3])
print(colours[-4])
# if we want to check any of the value present in the list 
data=["red","yellow",9.8,"python"]
if 9.8 in data:
    print("yes its present")
else:
    print("no its not present")
# printing elements in particular range
data=["red","yellow",9.8,"python",5,6,7,99]
# print(listname[start:end])
print(data[3:8])
print(data[2:6])
# print(listname[start:end:jumpindex])
print(data[1:5:2])
# print(listname[0:len(data)])
print(data[:])

# list comprehension
# syntax=list=[expression(item) for item in iterable if condition]
# example 1
lst=[i for i in range(4)]
print(lst)
lst=[i*i for i in range(20) if i%2==0]
print(lst)
# example 2
names=["milo","sarah","bruno","anastasia","rosa"]
nameswith_0=[item for item in names if "o" in item]
print(nameswith_0)


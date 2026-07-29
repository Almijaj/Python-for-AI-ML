# tuple is a set of elements which are seaprated by commas and written in round brackets and its unchangeable
# example 1
tup=(1,2,12,34,56,78)
print(type(tup),tup)
# example 2
details=("Abhijeet",18,"FYBscIT",9.8)
print(details)
# indexing
print(tup[0]) 
print(tup[1])
print(tup[3])
print(tup[5])
print(tup[-1])
print(tup[-4])
# check for item in the tuple
tup=("spain","itlay","england","india","germany")
if "germany" in tup:
    print("yes its present")
else:
    print("no its present")
# range of index
# tuple[start:end:jump index]
animals=("cat","dog","bat","mouse","pig","horse","donkey","goat","cow")
print(animals[3:7])
print(animals[-7:-2])
print(animals[1:8:3])
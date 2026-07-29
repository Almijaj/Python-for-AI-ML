# 1.Create a tuple of 5 numbers and print all the elements using a loop.
numbers=(1,2,3,4,5)
for i in numbers:
    print(i)
# 2.Find the length of a tuple.
numbers=(1,2,3,4,5)
print(len(numbers))
# 3.Print the first and last element of a tuple.
numbers=(1,2,3,4,5)
print("first element:",numbers[0])
print("first element:",numbers[4])
# 4.Count how many times a particular number appears in a tuple.
numbers=(10,20,30,20,40,20)
print(numbers.count(20))
# 5.Find the index of an element in a tuple.
numbers=(10,23,45,67,89)
print(numbers.index(45))
# 6.Find the maximum and minimum element in a tuple.
numbers=(10,20,30,40,50)
maximum=max(numbers)
minimum=min(numbers)
print("maximum numbers:",maximum)
print("minimum numbers:",minimum)
# 7.Calculate the sum of all elements in a tuple.
numbers=(10,20,30,40,50)
sum=numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]
print("sum of all elements",sum)
# 8.Convert a tuple into a list and then add a new element.
numbers=(10,20,30,40,50)
temp=list(numbers)
temp.append(60)
numbers=tuple(temp)
print(numbers)
# 9.Convert a list into a tuple.
list=[10,20,30,"harry"]
temp=tuple(list)
print(temp)
# 10.Reverse a tuple.
numbers=(10,20,30,40,50)
reverse=numbers[::-1] #so here there is [start:stop:step]
print(reverse)
# 11.Create a set and print all the elements.
info={"clara",9.5,"false",19,9.5}
print(info)
# 12.Add a new element to a set.
info={"Almijaj",21,8.76,"hello"}
info.add(99)
print(info)
# 13.Remove an element from a set.
info={"Almijaj",21,8.76,"hello"}
info.remove(21)
print(info)
# 14.Check whether an element exists in a set.
info={"Almijaj",21,8.76,"hello"}
if "Almijaj" in info:
    print("yes  it is present")
else:
    print("no its not")
# 15.Find the length of a set.
info={"hello",65,7.8,0.54}
print(len(info))
# 16.Find the union of two sets.
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.union(cities2)
print(cities3)
# 17.Find the intersection of two sets.
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.intersection(cities2)
print(cities3)
# 18.Find the difference between two sets.
a={1,2,3,4,5}
b={3,2,6,7,8}
c=a.symmetric_difference(b)
print(c)
# 19.Find the symmetric difference.
a={20,54,67,78}
b={54,78,32,45}
a.symmetric_difference_update(b)
print(a)
# 20.Remove duplicate values from a list using a set.
numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print(unique_numbers)
# 21.Check whether two tuples are identical.
tuple1=(20,30,40)
tuple2=(20,30,40)
if tuple1==tuple2:
    print("yes it is identical")
else:
    print("no its not identical")
#if there would be different values then it would show else statement
# 22.Find common elements between two tuples.
tuple1=(20,60,70)
tuple2=(20,30,40)
common=set(tuple1).intersection(set(tuple2))
print(tuple(common))
# 23.Take 10 numbers from the user and print only the unique numbers.
numbers = set()

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Unique numbers:", numbers)
# 24.Count how many unique words are present in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Number of unique words:", len(unique_words))
# 25.Find duplicate elements in a list using sets.
numbers = [10, 20, 10, 30, 20, 40]

seen = set()
duplicates = set()

for i in numbers:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicate elements:", duplicates)
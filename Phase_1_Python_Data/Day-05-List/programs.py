# 1.Print all elements of a list.
list=["red","yellow","green","blue","violet"]
print(list)
# 2.Find the length of a list.
list=["sunday","monday","tuesday","wenesday","thrusday","friday","saturday"]
print("length =",len(list))
# 3.Find the largest element.
number=[1,2,3,4,5,6,7]
largest=number[0]
for i in number:
    if i > largest:
        largest=i
print("largest elemnt=",largest)
# 4.Find the smallest element.
number=[1,2,3,4,5,6,0]
smallest=number[0]
for i in number:
    if i < smallest:
        smallest=i
print("smallest number=",smallest)
# 5.Calculate the sum of all elements.
numbers=[1,2,3,4,5,6]
sum=0
for i in numbers:
        sum=sum+i
print("sum of all elements",sum)
# 6.Find the average.
numbers=[10,20,30,40]
sum=0
for i in numbers:
    sum=sum+i
    average=sum/4
print("average of numbers",average) 
#7.Count even and odd numbers.
numbers=[10,33,45,62,22]
count1=0
count2=0
for i in numbers:
     if(i%2==0):
        count1=count1+1
     elif(i%2!=0):
          count2=count2+1
print("number of even numbers",count1)
print("number of odd numbers",count2)
# 8.Remove duplicate elements.
numbers=[21,34,56,65,21,34]
new_list=[]
for i in numbers:
     if i not in new_list:
      new_list.append(i)
print("new list by removing duplicates",new_list)
# 9.Reverse the list.
days=["sunday","monday","tuesday","wenesday","thrusday","friday","saturaday"]
days.reverse()
print(days)
# 10.Sort the list without using sort()
numbers = [40, 10, 30, 20]

sorted_list = []

while numbers:

    smallest = numbers[0]

    for i in numbers:
        if i < smallest:
            smallest = i

    sorted_list.append(smallest)
    numbers.remove(smallest)

print(sorted_list)
# 11.Find the second largest element.
numbers = [10, 45, 67, 23, 12]

largest=numbers[0]
for i in numbers:
    if i > largest:
        largest=i

second_largest=numbers[0]
for i in numbers:
    if i!=largest:
        if i>second_largest:
            second_largest=i
print("second largest",second_largest)
# 12.Merge two lists.
list1=[12,23,34,56,78]
list2=[33,55,66,99]
list1.extend(list2)
print(list1)
# 13.Remove all negative numbers.
numbers = [1, 2, -3, 4, 5, -9]

new_list = []

for i in numbers:
    if i > 0:
        new_list.append(i)

print("After removing negative numbers:", new_list)
# 14.Rotate a list by one position.
numbers = [10, 20, 30, 40, 50]

last = numbers[-1]
new_list = [last]

for i in range(len(numbers) - 1):
    new_list.append(numbers[i])

print(new_list)
# 15.Find duplicate elements.
numbers = [15, 14, 19, 15]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("Duplicate number:", numbers[i])
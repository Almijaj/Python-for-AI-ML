# 1.Create a dictionary containing: Name,Age,City,Course
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
print(info)
#2. Print only the name from the dictionary.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
print(info["Name"])
# 3.Print all the keys.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
print(info.keys())
# 4.Print all the values.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
print(info.values())
# 5.Add a new key called "email".
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
info.update({"email":"xyz@gmail.com"})
print(info)
# 6.Update the person's age.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
info.update({"Age":23})
print(info)
# 7.Delete one key from the dictionary.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
info.pop("Age")
print(info)
# 8.Check whether "age" exists in the dictionary.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}

if "Age" in info:
    print("Yes, it is present.")
else:
    print("No, it is not present.")
# 9.Find the number of key-value pairs in a dictionary.
info = {
    "Name": "Karan",
    "Age": 21,
    "City": "Ichalkaranji",
    "Course": "Robotics"
}
print("Number of key-value pairs =", len(info))
# 10.Loop through the dictionary and print:Name: Almijaj,Age: 20,City: Pune
info={"Name": "Almijaj","Age": 20,"City": "Pune"}
for key, value in info.items():
    print(key +   ":", value)
# 11.Create a dictionary containing 5 students and their marks.
students= {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 91,
    "John": 68,
    "Sara": 88
}
highest = 0

for i in students:
    if students[i] > highest:
        highest = students[i]

print("Highest mark =", highest)
# 12.Using the same dictionary, find the lowest mark.
students= {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 91,
    "John": 68,
    "Sara": 88
}
lowest = students["Rahul"]

for i in students:
    if students[i] < lowest:
        lowest = students[i]

print("lowest mark =", lowest)
# 13.Calculate the average marks of all students.
students= {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 91,
    "John": 68,
    "Sara": 88
}
sum=0
for i in students:
   sum=students[i]+sum
average=sum/5
print("average marks=",average)
# 14.Count how many students scored more than 80.
students= {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 91,
    "John": 68,
    "Sara": 88
}
count=0
for i in students:
    if students[i] >80:
        count=count+1
print(count)
# 15.Take a sentence from the user and count how many times each word appears.
sentence = input("Enter a sentence: ")

words = sentence.split()

count = {}

for i in words:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count)
# 16.Create a dictionary containing numbers and their squares.
numbers = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

print(numbers)
# 17.Create a dictionary that counts the frequency of each number.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count={}
for i in numbers:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)
# 18.Find the student with the highest marks.
students= {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 91,
    "John": 68,
    "Sara": 88
}
highest = 0
student = ""
for i in students:
    if students[i] > highest:
        highest = students[i]
        student=i
print("Student with highest marks =", student)
print("Highest mark =", highest) 
# 19.Take student names and marks from the user and store them in a dictionary.
students={}
for i in range (3):
    name=input("enter the name of student")
    marks=int(input("enter the marks of the student"))
    students[name]=marks
print(students)
# 20.Create a simple phone book.
phonebook = {}

while True:
    print("\n===== PHONE BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    

    choice=int(input("enter the choice:"))

    if choice == 1:
        name=input("enter the name=")
        number=int(input("enter the number="))
        phonebook[name]=number
        print("Contact added successfully!")

    elif choice == 2:
        name=input("enter the name=")
        if name in phonebook: 
            print("Phone Number:",phonebook[name])
        else:
            print("Contact not found.")
    elif choice == 3:
        name = input("Enter the name: ")
        if name in phonebook: 
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == 4:
       if len(phonebook) == 0:
            print("Phonebook is empty.")
       else:
            print("\nAll Contacts:")
            for name, number in phonebook.items():
                print(name, ":", number)

    elif choice == 5:
        print("thank you!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
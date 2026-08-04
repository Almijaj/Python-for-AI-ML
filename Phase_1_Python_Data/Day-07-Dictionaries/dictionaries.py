# python dictionaries:this are ordered collection of data items.they store multiple values in a single variable they are enclosed within {}
info={
    "name":"karan",
    "age":"nineteen"
    }
print(info) #for printing whole value
# example
dic={
    564:"arsh",
    43:"soyo",
    56:"zaya",
    567:"neha"
}
print(dic[43]) #for printing the mentioned value ,this throws an error
print(dic.get(434))#this doesnt throws an error
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(dic[key])

for key in dic.keys():
    print(f"the corresponding to the key {key} is {dic[key]}")

# accesing keys
info={'name':'karan','age':19,'eligible':'true'}
print(info.items())
for key ,value in info.items():
    print(f"the value corresponding to the key {key} is {value}")

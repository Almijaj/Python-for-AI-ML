# update():updates the values of key provided in the item already exist in the dictionaries 
info={"name":"karan","age":19,"eligible":"true"}
print(info)
info.update({"age":21})
info.update({"name":"harry"})
print(info)
# clear():clears the list
info.clear()
print(info)
# for printing the empty dictionaries
empt={}
print(empt)
# pop():removes the key value pairs
info={"name":"karan","age":19,"eligible":"true"}
info.pop("eligible")
print(info)
# popitem():removes the last key value pair from the dictionaries
info={"name":"karan","age":19,"eligible":"true"}
info.popitem()
print(info)
# del : its deletes the entire dictonaries 
info={"name":"karan","age":19,"eligible":"true"}
del info
del info["name"]
print(info) 

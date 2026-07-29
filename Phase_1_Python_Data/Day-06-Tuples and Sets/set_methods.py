# union() and update()
# union():its basically used to merge two sets 
# update():its basically used to update the set
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.union(cities2)
print(cities3)
cities3=cities1.update(cities2)
print(cities3)
# intersection() and intersection_update():so basically this prints only the items that are similar to both the sets the intersection() 
# method returns a new set whereas intersection_update() upadates into the existing set from the another set 
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.intersection(cities2)
print(cities3)
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities1.intersection_update(cities2)
print(cities1)
# symmetric_difference() and symmetric_difference_update():so this prints the values which are not common 
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.symmetric_difference(cities2)
print(cities3)
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities1.symmetric_difference_update(cities2)
print(cities1)
# difference() and difference_update():prints only item that are only present in the original set and not in both set 
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul"}
cities3=cities1.difference(cities2)
print(cities3)
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul"}
cities1.difference_update(cities2)
print(cities1)
# there are several in-built methods for manipulation of set.
# isdisjoint()=checks weather there is intersection or not and writtens false and true
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Berlin"}
print(cities1.isdisjoint(cities2)) 
# issuperset()=checks if all the items of a particular set are present in the subset 
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Seoul","Kabul"}
print(cities.issuperset(cities2))
cities3={"Seoul","Madrid","Kabul"}
print(cities.issuperset(cities3))
# issubset()=checks if all the items in the original set are present in the particular set.
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Delhi","Madrid"}
print(cities2.issubset(cities))
# add()=if you want to add a single item in set use add() method
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.add("Helsinki")
print(cities)
# update()=if you want to add more than one items 
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Helsinki","Warsaw","Seoul"}
cities.update(cities2)
print(cities)
# remove()/discard()=we can use it for removing the items ,if we want to through errors we can use remove() and if not use discard()
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
cities.discard("Tokyo1")
print(cities)
# pop()=this removes last item in the set but we dont know which item gets popped as set is unordered 
cities={"Tokyo","Madrid","Berlin","Delhi"}
item=cities.pop()
print(cities)
print(item)
# del=its a keyword that deletes the set entirely
cities={"Tokyo","Madrid","Berlin","Delhi"}
del cities
print(cities)
# clear()=so this deletes the items in the set and make it empty
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.clear()
print(cities)
# check if item exist
info={"Clara",19,False,5.9}
if "Clara" in info:
    print("clara is present")
else:
    print("clara is absent")
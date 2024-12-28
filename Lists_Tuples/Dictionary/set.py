# Set
collection={1,2,3,4,2,3,"promi","riya","promi"}
print(collection)
print(type(collection))
#list
# my_list = [1, 2, 3, 4]
# my_list.append(5)
# print(my_list)
# Dictionary
# info={
#     "name":"Anabia",
#     "age":3,
#     "city":"Dhaka"
# }
# print(info["name"])
# # tuple
# tup=(2,12,4,5,2,14)
# print(type(tup))

# empty set
col=set()
print(col)

# method of set
my_collection=set()
my_collection.add(1)
my_collection.add(2)
my_collection.add((3,4,5)) # tuple add
my_collection.remove(1)
my_collection.clear() # empty the set
print(my_collection)
#In set tuple can be added,list and dictionary can not be added
#popn remove random value
# my_collection.pop()


set1={1,2,3,4}
set2={3,4,5,6,7}
print(set1.union(set2))
print(set1.intersection(set2))
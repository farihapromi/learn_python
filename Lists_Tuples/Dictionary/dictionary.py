info={
    "name":"Anabia",
    "age":3,
    "city":"Dhaka"
}
print(info["name"])
#in dictionary we can also do lists ,tuple
# my_dict={
#     "name":"Promi",
#     "subject":["cse","Physics","Chemistry"],
#     "marks":(12,45,78,90),
#     "city":"Dhaka"
# }
# print(my_dict["subject"])
# Nested dictionary

my_dict={
    "name":"Promi",
    "subject":{
        "name":"CSE",
        "range":4,  
        "University":"Ju"      
    },
    "marks":(12,45,78,90),
    "city":"Dhaka"
}
print(my_dict["subject"])
print(my_dict["subject"]["name"])
print(list(my_dict.items()))
print(my_dict.get("marks"))

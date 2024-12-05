# mov1=input("enter first movie 1")
# mov2=input("enter first movie 2")
# mov3=input("enter first movie 3")
# list=[]
# list.append(mov1)
# list.append(mov2)
# list.append(mov3)
# print(list) 

 #copy reverse is planidrom
my_list1=[1,"abc","abc",1]

list=my_list1.copy()
list.reverse()
if(list== my_list1):
    print("Palindrom")
else:
    print("Not Palindrom")
    

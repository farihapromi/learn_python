# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

#write filr
f=open("demo.txt","w")
data=f.write("Lets leanr javasccript")
print(data)
f.close()
f=open("demo.txt","a")
data=f.write("\n This add new things")
print(data)
f.close()
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
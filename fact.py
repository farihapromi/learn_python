# def cal_fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*cal_fact(n-1)
# print(cal_fact(4)) 
#Calculate sum using recursion
def cal_sum(n):
    if(n==0):
        return 0
    
    return cal_sum(n-1) + n
print(cal_sum(7))  
 #function to print list element using recursion
 
def print_list(list,idx):
    if(idx== len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","banana","lichi","grapes"]   
print_list(fruits,0) 
     
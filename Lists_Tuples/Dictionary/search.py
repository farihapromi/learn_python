# nums=(34,56,7,8,9)
# x=7
# i=0
# while i<len(nums):
#     if(nums[i]== x):
#         print("index found at ",i)
#         break
#     i+=1
# else:
#     print("not found")
nums = (34, 56, 7, 8, 9)
x = 7
i = 0

while i < len(nums):
    if nums[i] == x:
        print("Index found at", i)
        break  # Exit the loop after finding the index
    i += 1  # Increment `i` on every iteration
else:
    print("Element not found")
    
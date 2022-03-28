def num(nums):
    i=0
    c=[]
    while i<len(nums):
        if nums[i] not in c:
            c.append(nums[i])  
        i=i+1
    c.sort()
    return c
print(num(nums=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]))


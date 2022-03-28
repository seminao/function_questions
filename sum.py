# list=[21,23,45,7,88,99]
# i=0
# a=[]
# while i<len(list):
#       k=list[i:i+2]
#       a.append(k)
#       i=i+2
# print(a)
# 
# 
# def sum(number):
#     i=0
#     s=0
#     while i<len(number):
#         s=s+number[i]
#         i=i+1
#     return s
# print(sum([1, 2, 3, 4, 5]))

# **sum of list 
def my(a):
    i=0
    c=[]
    while i<len(a):
        j=0
        s=0
        while j<len(a[i]):
            s=s+a[i][j]
            j=j+1
        c.append([s])
        i=i+1
    return c
print(my([[1,4],[5,2],[7,6],[8,1]]))


def product(number):
    i=0
    p=1
    while i<len(number):
        p=p*number[i]
        i=i+1
    return p
print(sum([1, 2, 3, 4, 5]))
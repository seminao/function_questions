# def my(list):
#     i=0
#     s=0
#     b=[]
#     while i<len(list):
#         b.append(list[i])
#         s=s+list[i]
#         c=[s]
#         i=i+1
#     print(b+c)
# my([1,2])

# def append(num):
#     l.insert(3,num)
#     return l
# l=[1,2,3]
# num=int(input("enter number:"))
# print(append(num))


# def append(num):
#     return l+[num]
# num=int(input("enter number:"))
# l=[1,2,3]
# print(append(num))
    
# def my(num):
#     i=0
#     a=[]
#     while i<len(num):
#         if num[i]==num[0]:
#             a.append(num[i])
#         i=i+1
#     if num==a:

#         print("True")
#     else:
#         print("False")
# my([1,1,1,1,1,1,8,1,1,1])

# def my(num):
#     s=[1,2]
#     print(s+[num])
# my(num=int(input("enter the number")))

# def my(num):
#     s=[1,2]
#     return s+[num]
# print(my(num=int(input("enter the number"))))

# def my(user):
#     i=0
#     while i<len(user)-1:
#         if user[i]==user[i+1]:
#             return True
#         i=i+1
#     return False
# print(my(user=input("enter the number: ")))

# def my(user):
#     i=0
#     while i<len(user)-1:
#         if user[i]==user[i+1]:
#             return True
#         i=i+1
#     return False
# print(my(user=input("enter the number: ")))



# user=input("enter your chr: ")
# i=0
# a1=0
# a2=0
# b1=0
# b2=0
# c1=0
# c2=0
# while i<len(user):
#     if user[i]=="(":
#         a1=a1+1
#     if user[i]==")":
#         a2=a2+1
#     if user[i]=="{":
#         b1=b1+1
#     if user[i]=="}":
#         b2=b2+1
#     if user[i]=="[":
#         c1=c1+1
#     if user[i]=="]":
#         c2=c2+1
#     i=i+1
# if a1==a2 and b1==b2 and c1==c2:
#     print(True)
# else:
#     print(False)

# def my(list):
#     i=0
#     c=0
#     while i<len(list):
#         if "ing" in list[i]:
#             c=c+1
#         i=i+1
#     print(c)
# my(["remebering","is","good","thinking"])
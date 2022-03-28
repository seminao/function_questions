# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# def my(alph):
#     i=0
#     a=[]
#     while i<len(alph):
#         if alph[i]==65-90:
#             a.append(alph[i])
#         i=i+1
#     alph.sort()
#     return alph
# print(my(alph=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]))

# *2 method
def my(alph):
    l=len(alph)-1
    i=l
    a=[]
    while i>=0:
        a.append(alph[i])
        i=i-1
    return a
print(my(alph=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]))

# *3 method
def my(alph):
    i=-1
    a=[]
    while i>=-(len(alph)):
        a.append(alph[i])
        i=i-1
    return a
print(my(alph=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]))


b="1234adcd"
# c=""
# i=-1
# while i>=-len(b):
#     c+=b[i]
#     i-=1
# print(c)


def reverse(list):
    i=-1
    c=""
    while i>=-len(list):
        c+=list[i]
        i-=1
    return c
print(reverse(("1234abcd"))) 

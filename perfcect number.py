# def perfect(x):
#     i=1
#     while i<=x:
#         sum=0
#         j=1
#         while j<i:
#             if i%j==0:
#                 sum+=j
#             j+=1
#         if sum==i:
#             print(i,"is perfect number") 
#         i+=1
# perfect(6)

# def perfect_number(n):
#     sum=0
#     for x in range (1,n):
#         if n%x==0:
#             sum+=x
#     return sum==n
# print(perfect_number(6))

def my(num):
    i=1
    s=0
    while i<=num:
        # s=0
        if num%i==0:
            s=s+i
        i=i+1
    if num==s:
        print(num,"is perfect number")
    else:
        print(num,"is not perfect number")
my(6)
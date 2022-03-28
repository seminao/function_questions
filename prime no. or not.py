# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)

def prime_no_or_not(num):
    i=1
    n=0
    while i<=num:
        if num%i==0:
            n=n+1
        i=i+1
    if n==2:
        print(num, "is prime number")
    else:
        print(num,"not")  
prime_no_or_not(num=int(input("enter the number")))
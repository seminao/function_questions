# Write a function that returns True if the number is a very even number.
# If a number is a single digit then it is simply "very even" 
# if it is even. If it has 2 or more digits, it is "very even" 
# if the sum of its digit is " very even"

num=int(input("enter the number"))
def my(num):
    if num<=9 and num%2==0:
        print("very even")
    elif num>=10:
        i=0
        s=0
        b=str(num)
        while i<len(b):
            c=int(b[i])
            s=s+c
            i=i+1
        return my(s)
    else:
        print(num,"odd")
my(num)


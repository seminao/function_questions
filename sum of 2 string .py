# o/p="4","5"="9"
def my(num):
    i=0
    s=0
    while i<len(num):
        s=s+int(num[i])
        i=i+1
    print("'",s,"'")
my(num=["4","5"])

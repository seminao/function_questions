def num(list):
    i=0
    s=0
    c=0
    avg=0
    while i<len(list):
        c=c+1
        s=s+list[i]
        avg=s//c
        i=i+1
    print(avg)
    return s
    
print(num(list=[3,4,5]))

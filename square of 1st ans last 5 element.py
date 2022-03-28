def my():
    i=1
    a=[]
    b=0
    while i<=30:
        b=i**2
        a.append(b)
        i=i+1
    print(a[:5],a[25:])
my()
# "the quick Brow Fox"
# o/p=upper:2
    # lower:13

def my(v):
    i=0
    c1=0
    c2=0
    while i<len(v):
        if str(v[i]).isupper():
            c1+=1
        elif str(v[i]).islower():
            c2+=1
        else:
            pass
        i=i+1
    return c1,c2
print(my("the quick Brow Fox"))
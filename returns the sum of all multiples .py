def my(num):
    i=0
    s1=0
    s2=0
    while i<=num:
        if i%3==0:
            s1=s1+i
        elif i%5==0:
            s2=s2+i
        i=i+1
    total_sum=s1+s2
    return total_sum
print(my(20))

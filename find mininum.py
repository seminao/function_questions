# list = [8, 6, 4, 8, 4, 50, 2, 7]

def my(num):
    i=0
    min=num[0]
    while i<len(num):
        if num[i]<min:
            min=num[i]
        i=i+1
    return min
print(my(num=[8, 6, 4, 8, 4, 50, 2, 7]))
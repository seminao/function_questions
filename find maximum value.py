# (*1 method)
def number(number):
    i=0
    max=0
    while i<len(number):
        if number[i]>max:
            max=number[i]
        i+=1
    return max
print(number([3,5,7,34,2,89,2,5]))

# *2method
number=[43,67,34,98,132,6,90]
print(max(number))
def eligible(age):
    if age >=18:
        print(age,"is eligible for voting")
    else:
        print("not eligible")
    return age
eligible(age=int(input("enter the number")))
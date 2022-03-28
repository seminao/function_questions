# language=input("language ")
# print("welcome to indian overseas bank")
# secretpin=input("enter the 4 digits pin code")
# if secretpin=="4667":
#     user_choose=input("withdrawl or balance enquiry or deposite")
#     balance=10000
#     if user_choose=="w":
#         amount=int(input("enter the amount"))
#         if amount <=5000:
#             print("processing")
#             print("transfer complet")
#             print(balance-amount,"left balance")
#         else:
#             print("cannot be withdraw")
#     if user_choose=="balance enquiry":
#         print("your current balance is",balance)
#     if user_choose=="deposite":
#         deposite=int(input("enter the deposite amount"))
#         print(deposite+10000,"is your current balance")
#     else:
#         print("thankq")
#         print("thank for visiting indian overseas bank")

option_language=["english","hindi","manipuri","thailand","koren"]
def code():
    user_choose=input("what do you want to do ")
    balance=10000
    if user_choose=="w" :
        amount=int(input("enter the amount"))
        user2=int(input("enter the secret_pin"))
        if user2==3456:
            print(balance-amount,"is your current balance")
    elif user_choose=="d":
        amount=int(input("enter the amount"))
        user2=int(input("enter the secret_pin"))
        if user2==3456:
            print(balance+amount,"is your current balance")
    elif user_choose=="balance_i":
        user2=int(input("enter the secret_pin"))
        if user2==3456:
            print(balance,"is your current balance")
            return "thank Q for visiting"
    else:
        print("wrong pin")
def choose():
    i=0
    while i<len(option_language):
        print("language=",option_language)
        user=input("enter the language")
        if user=="english" or "hindi":
            print("welcome to indian overseas bank")
            print(code())
            break
        
        i=i+1
choose()

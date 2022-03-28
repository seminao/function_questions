# import random
# user_action=input("enter the number(rock,paper, sessiors :")
# possible_action=["rock","paper" ,"sessiors"]
# computer_choice=random.choice(possible_action)

# if user_action==computer_choice:
#     print("draw")
# elif user_action=="rock":
#     if computer_choice=="paper":
#         print("winner becz rock can be cover by paper ")
#     else:
#         print("scissors smashes!you lose")
# elif user_action=="scissors":
#     if computer_choice=="paper":
#         print("winner becz paper can be cut by scissors" )
#     else:
#         print("rock smeshes scissors!you lose")
# elif user_action=="paper":
#     if computer_choice=="scissors":
#         print("loser bcz paper cn be cut by scissors")
#     else:
#         print("rock cover paper!win")

def even_num(num):
    if len(str(num))==1:
        if num%2==0 or num==0:
            print("it is a very even number")
        else:
            print("this is not a even number")
    else:
        sum=0
        num=str(num)
        for digit in num:
            sum+=int(digit)
        if sum%2==0:
            print(sum,"is a very even number")
        else:
            print(sum,"is not a even number")
even_num(555)

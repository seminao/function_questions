# gobal variable
message="how you doing"
def greet():
    print(message)
greet()

# local variable
message="how you doing"
def greet():
    message="how are you?"
    print("message outside",message)
greet()
print("message inside",message)
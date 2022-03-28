# def say_hello_language(name, language):
#     if language == "nambashi":
#         print("shakthibi ", name)
#         print("nim a dem mae?")
#     elif language == "Manipuri":
#         print("phajabi ", name)
#         print("kei douregae")
#     else:
#         print("i love you", name)
#         print("yes/no")
# say_hello_language("themshingla", "Manipuri")
# say_hello_language("Dew", "english")
# say_hello_language("shangkhurei", "nambashi")
# say_hello_language("Kavay", "hindi")

# ************
# def say_hello_people(name_x, name_y, name_z, name_a,name_b):
#     print("seminao=", name_x) 
#     print("mashotmi=", name_y) 
#     print("victor=", name_z)  
#     print("ngathingwon=", name_a)
#     print("chihangam=", name_b) 
# # say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# # say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")
# say_hello_people("Eveizolo","khurumjare","maringphalikhalae","swadikha","ola")

# def my(name,age):
#     print(name+" "+ "is"+ " "+age+" "+ "years"+" "+ "old")
# my("dew","22")

#  My name is Rishabh..
# I am the co-founder of NavGurukul.
# def new_line(name,hostel):
#     print("my name is",name)
#     print("i am the co-founder of",hostel)
# new_line("abishak","navgurukul")

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)

# *
# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")

# *using for loop 
# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))
# print(meal("other","lunch"))

# def checkKey():
#     frinds ={"seminao":  "vilychon","katimla":  "mustang","year":  1964}
#     if "themshingla" in frinds:
#         print("Yes, 'themshingla' is their.")
#     else:
#         print("No, 'themshingla'  left their frnd and find a big job with salary 1lakh in the yr 2022.")
# checkKey()

# def bmi(name,weight,height):
#     if 

# list=["2",4,6,"3",4,"9",3]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==int:
#         d=int(list[i])**2 
#         a.append(d)
#     elif type (list[i])==str:
#         c=int(list[i])**2
#         a.append(c)
#     i=i+1
# print(a)

# def my(num):
#     i=0
#     c=0
#     while i<len(num):
#         if num[i]%2==0:
#             c=c+1
#         i=i+1
#     print(c)
# my(num=[28,10,8,33,45,20])

# def my(num):
#     if num<=9 and num%2==0:
#         print("very even")
#     elif num>=10:
#         i=0
#         s=0
#         b=str(num)
#         while i<len(b):
#             c=int(b[i])
#             s=s+c
#             i=i+1
#         return my(s)
#     else:
#         print("is odd")
# my(555)

# num=1
# def fun():
#     globle num
#     num=num+3
# func()
# print(num+2)

# def t(x=1,y=2):
#     x=x+y
#     y+=1
#     print(x+y)
# t()

# def c():
#     x=1
#     while x<10:
#         x=x+1
#     print(x)
# c()

# d=5
# def a(x,y):
#     print(x+y)
#     return d+x
# p=a(2,4)
# def m(n,o):
#     return p
# print(m(2,3))

# def here(a,b):
#     total=a+b
#     return total,"sum"
# a=50
# b=20
# print(here(23,89))
# r=here(a,b)
# print(r)

# def my():
#     string=input("enter the string")
#     p=list(string)
#     k=len(p)
#     i=-1
#     a=[]
#     while i>=-k:
#         a.append(p[i])
#         i-=1
#     if a==p:
#         print("palindrome")
#     else:
#         print("not palindrome")
#     print(a)
# my()


# def my():
    # amount=int(input("enter the amount"))
    # if amount


# dollar=int(input("enter the amount"))
# rupe=int(input("enter the number"))
# def my(dollar):
#     mul=dollar*rupe
#     print(mul)
# def my1(rupe,dollar):
#     mul1=rupe*dollar
#     print(mul1)

# def my_1():
#     if dollar==0:
#         return my()
#     elif rupe==1:
#         return my1()
        
# my_1()

# def rup(doll):
#     print(doll,"dollar=",doll*72,"in rupee")
# doll=int(input("enter the number"))
# rup(doll)

# dollar=int(input("enter the number"))
# user=int(input("enter 0 to convert india rupe into dollar,1 to dollar into rupe "))

# def rup(dollar):
#     print(dollar,"dollar=",dollar*75,"in rupee")
# def my(dollar):
#     print(dollar,"is=",75/dollar, "dollar")
# def new():
#     if user==0:
#         return rup(dollar)
#     else:
#         return my(dollar)
# new()

# def my(num):
#     i=0
#     c=0
#     while i<len(num):
#         if num[i]%2==0:
#             c=c+1
#         i=i+1
#     print(c)
# my(num=[28,10,8,33,45,20]) 





# h=[4,2,7,10,5,9,7,20,6]
# a=[]
# c1=0
# c2=0
# c3=0
# c4=0
# c5=0
# c6=0
# c7=0
# c8=0
# i=0
# while i<len(h):
#     if h[i]>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [0]:
#         c1=c1+1
#     elif h[i]>h[i][1]:
#         c2=c2+1
#     elif h[i]>h[i][2]:
#         c3=c3+1
#     elif h[i]>h[i][3]:
#         c4=c4+1
#     elif h[i]>h[i][4]:
#         c5=c5+1
#     elif h[i]>h[i][5]:
#         c6=c6+1
#     elif h[i]>h[i][6]:
#         c7=c7+1
#     elif h[i]>h[i][7]:
#         c8=c8+1
#     elif h[i]>h[i][8]:
#         c9=c9+1
#     a.append(c1,c2,c3,c4,c5,c6,c7,c8,c9)
#     i=i+1
# print(a)




# num=int(input("enter the number"))
# a=[]
# for n in range (num):
#     n=int(input("enter the number"))
#     a.append(n)
# print(a)
# print(max(a))
# print(min(a)

# n=int(input("enter the number"))
# i=0
# min=1000
# max=0
# while i<n:
#     num=int(input("enter the number"))
#     if num>max:
#         max=num
#     elif num<min:
#         min=num

#     i=i+1
# print(max)
# print(min)

# h=[4,2,7,10,5,9,7,20,6]
# a=[]
# i=0
# while i<len(h):
#     j=0
#     c=0
#     while j<lens="A man, a plan, a canal:Panama"
# a=""
# b=""
#
# while i<len(s):
#     if s[i]!="," and s[i]!=" " and s[i]!=":":
#         a+=s[i]
#     i+=1
# b+=a.lower()
# j=-1
# c=""
# while j>=(-(len(b))):
#     c+=(b[j])
#     j-=1
# print(c)
# if b==c:
#     print(True)
# else:
#     print(False)
# (h):
#         if h[i]<h[j]:
#             c+=1
#         j=j+1
#     i=i+1
#     a.append(c)
# print(a)


# s="A man, a plan, a canal:Panama"
# a=""
# b=""
# i=0
# while i<len(s):
#     if s[i]!="," and s[i]!=" " and s[i]!=":":
#         a+=s[i]
#     i+=1
# b+=a.lower()
# j=-1
# c=""
# while j>=(-(len(b))):
#     c+=(b[j])
#     j-=1
# print(c)
# if b==c:
#     print(True)
# else:
#     print(False)



# *logic Q.
# x=4
# y=x+x
# def s(p,q):
#     i=0
#     while i<=2:
#         print(x)
#         i=i+1
#     print(y)
#     return i
# print(s(4,3))


# user=int(input("enter your number: "))
# num=[2,3,4,5,6,8,1]
# i=0
# a=[]
# while i<len(num):
#     j=0
#     b=[]
#     while j<len(num):
#         sum=num[i]+num[j]
#         if sum==user:
#             b.append(i)
#             b.append(j)
#         j=j+1
#     a.append(b)
#     i=i+19
# print(a)

# a=[1000,464,768,240,56]
# c=[]
# i=0
# while i<len(a):
#     b=str(a[i])
#     l=list(b)
#     c.append(l)
#     i+=1
# d=[]
# j=0
# while j<len(c):
#     f="".join(c[j])
#     d.append(int(f))
#     j=j+1
# print(d)

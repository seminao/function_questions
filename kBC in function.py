# question_list=["How many continents are there ?","What is the capital of India ?",
# "NG mei kaun se course padhaya jaata hai ? "]
# options_list=[["Four","Nine","Seven","Eight"],
# ["Chandigarh","Bhopal","Chennai","Delhi"],
# ["Software Engineering","Counseling","Tourism","Agriculture"]]
# life_line=[["Seven","Eight"],["Bhopal","Delhi"],["SoftwareEngineering","Counseling"]]
# solution_list2=[1,2,1]
# i=0
# count=0
# solution_list=[3,4,1]
# while i<len(question_list):
# 	print("Q.",i+1,question_list[i])
# 	j=0
# 	while j<len(options_list[i]):
# 		print(j+1,options_list[i][j])
# 		j=j+1
# 	user=int(input("enter any number: "))
# 	if user==solution_list[i]:
# 		print("congrates your answer is correct")
# 	elif user==5050:
# 		if count==0:
# 			k=0
# 			while k<len(life_line[i]):
# 				print(k+1,life_line[i][k])
# 				k=k+1
# 			count=count+1
# 			user2=int(input("enter any number. "))
# 			if user2==solution_list2[i]:
# 				print("you answer is right")
# 			else:
# 				print("wrong answer:")
# 		else:
# 			print("you already used the 5050 chance")
# 			num=int(input("enter any number: "))
# 			if num==solution_list[i]:
# 				print("right answer")
# 			else:
# 				print("wrong answer")
# 				break
# 	else:
# 		print("Your answer is wrong")
# 		break
# 	i=i+1

question_list=["Which out the following is a scripting language??","What is the capital of India ?",
"Which of the following is the first calculating device? ? ","Who invented mechanical calculator called Pascaline?"]

options_list=[["Java","Python","Lisp","All of the above","None of the above"],
["Chandigarh","Bhopal","Chennai","Delhi","Hint option"],
["Abacus","Calculator","Turing Machine"," Pascaline","Hint option"]
,["Charles Babbage"," Blaise Pascal"," Alan Turing","Lee De Forest"]]

Hint_option=[["None of the above","All of the above"],["Bhopal","Delhi"],["Abacus","Pascaline"],["Blaise Pascal","Charles Babbage"]]

Hint_solution=[2,2,1,1]
solution_list=[4,4,1,2]
count=0

def hint(i):
	global count
	if count==0:
		k=0
		while k<len(Hint_option[i]):
			print(k+1,Hint_option[i][k])
			k=k+1
		answer=int(input("enter any no. "))
		count=count+1
		if answer==Hint_solution[i]:
			return True
		else:
			return False
	else:
		print("you already used hint option")
		option(i)

def option(i):
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1 
	ans=int(input("enter your answer: "))
	if ans==solution_list[i]:
		return True
	if ans==5:
		return hint(i)
	else:
		return False
	
def  question():
	i=0
	while i<len(question_list):
		print("Q.",i+1,question_list[i])
		x=option(i) 
		if x==True:
			print("your ans is correct")
		elif x==False:
			print("you lose the game")
			break
		i=i+1
question()

# question_list=["Which out the following is a scripting language??","What is the capital of India ?",
# "Which of the following is the first calculating device? ? ","Who invented mechanical calculator called Pascaline?"]
# options_list=[["Java","Python","Lisp","All of the above","None of the above"],
# ["Chandigarh","Bhopal","Chennai","Delhi","Hint option"],
# ["Abacus","Calculator","Turing Machine"," Pascaline","Hint option"]
# ,["Charles Babbage"," Blaise Pascal"," Alan Turing","Lee De Forest"]]

# hint_option=[["None of the above","All of the above"],["Bhopal","Delhi"],["Abacus","Pascaline"],["Blaise Pascal","Charles Babbage"]]
# solution_list=[4,4,1,2]
# solution_hint=[2,2,1,1]
# count=0

# def hint(i):
# 	globle count
# 	if count==0:
# 		k=0
# 		while k<len(hint_option[i]):
# 			print(k+1,hint_option[i][k])
# 			k=k+1
# 		ans=int(input("enter the number"))
# 		count=count+1
# 		if ans==solution_hint[i]:
# 			return True
# 		else:
# 			return False
# 	else:
# 		print("you already use life_line")

# def option(i):
# 	j=0
# 	while j<len(options_list[i]):
# 		print(j+1,options_list[i][j])
# 		j=j+1
# 		ans2=int(input("enter the number"))
# 		if ans2==solution_list[i]:
# 			return True
# 		elif ans2==5:
# 			return hint(i)
# 		else:
# 			return False
# def my():
# 	i=0
# 	while i<len(question_list):
# 		print("Q.",i+1,question_list[i])
# 		x=option(i)
# 		if x==True:
# 			print("your ans is correct")
# 		else:
# 			print("your ans is wrong")
# 			break
# 		i=i+1
# my()
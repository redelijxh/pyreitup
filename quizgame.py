import os
from random import shuffle

def menu():
	print("---------------------------")
	print("|  PYRE IT UP! QUIZ GAME  |")
	print("---------------------------\n")
	print("[1] START Quiz")
	print("[2] View High Scores")
	print("[3] Reset High Scores")
	print("[0] Exit")
	choice = int(input("\nChoice: "))
	return choice

def category_menu():
	print("---------------------------")
	print("|     SELECT CATEGORY     |")
	print("---------------------------\n")
	print("[1] Ultimate Frisbee")
	print("[2] League of Legends")
	print("[3] KPOP")
	print("[0] Exit\n")
	category_choice = int(input("Choice: "))
	return category_choice

def difficulty_menu():
	print("---------------------------")
	print("|    SELECT DIFFICULTY    |")
	print("---------------------------\n")
	print("[1] Kindle\t(EASY)") 
	print("[2] Flamin'\t(MEDIUM)")
	print("[3] Scorched\t(HARD)")
	print("[0] Exit\n")
	difficulty_choice = int(input("Choice: "))
	return difficulty_choice

def instructions(scoring):
	inst="Each round consists of 10 random questions from each category.\nChoose the letter of the correct answer."+"\nEach correct answer is worth "+str(scoring)+" point/s."+"\nGood luck!\n"
	return inst

def quizgame(question_file,points):
	instpoint=points
	fileReader=open(question_file,"r")
	question_roster=[]
	
	for line in fileReader:
		list1=line[:-1].split(",")
		question_roster.append(list1)
	
	fileReader.close()	
	
	score=0
	name=input("Enter name: ")
	name=name.capitalize()
	print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("|      QUIZ STARTS        |")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	inst=instructions(instpoint)
	print(inst)
	
	shuffle(question_roster)
	displayed_questions=0

	while displayed_questions != 10:
		correctAns=question_roster[displayed_questions][0]
		ques=question_roster[displayed_questions][1]
		choiA=question_roster[displayed_questions][2]
		choiB=question_roster[displayed_questions][3]
		choiC=question_roster[displayed_questions][4]
		print(ques)
		print()
		print("[A]",choiA)
		print("[B]",choiB)
		print("[C]",choiC)

		userAns=input("\nAnswer: ")
		print()
		userAns=userAns.upper()
		if userAns==correctAns:
			score=score+points
			print("\tCorrect!\n")
		else:
			print("\tThe correct answer is",correctAns,"\n")	
		#increment	
		displayed_questions=displayed_questions+1	

	return name,score	

def selection_sort(x):
	for i in range(len(x)):
		minimum= i
		for j in range (i+1,len(x)):
			if x[minimum][1] < x[j][1]:
				minimum=j
		temp= x[minimum]
		x[minimum]=x[i]
		x[i]=temp
	return x

def name_check(mainList,username,userscore):
	
	inTheList=False

	for i in mainList:
		if username==i[0]:
			inTheList=True
			break
	if inTheList:
		i[1]=i[1]+userscore
		# print(i)
	else:
		newInput=[name,score]
		mainList.append(newInput)

	return mainList	

#MAIN PROGRAM

choice = None
highscore_list=[]

#Auto Load High Score
fileDisplay=open("highscore_roster.txt","r")
for line in fileDisplay:
	list1=line[:-1].split(",")
	list1[1]=int(list1[1])
	

	if highscore_list==[]:
		highscore_list.append(list1)
	elif list1 in highscore_list:
		continue
	else:
		highscore_list.append(list1)
		
fileDisplay.close()

while choice!=0:
	
	choice = menu()
	un = os.system('cls')

	if choice==1:

		difficulty_choice=None
		
		while difficulty_choice!=0:
			difficulty_choice=difficulty_menu()

			if difficulty_choice ==1:
				print("\nYou have chosen EASY\nPlease choose a category\n")
				
				category_choice=None
				while category_choice != 0:
					category_choice=category_menu()
		
					if category_choice==1:
						un = os.system('cls')
						print("\nEASY:Ultimate Frisbee\n")
						name,score=quizgame("easy_frisbee.txt",1)
						print()
						print(name,"scored:",score)
						print()

						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0
					
					elif category_choice==2:
						un = os.system('cls')
						print("\nEASY:League of Legends\n")
						name,score=quizgame("easy_league.txt",1)
						print()
						print(name,"scored:",score)
						print()

						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0

					elif category_choice==3:
						un = os.system('cls')
						print("\nEASY:KPOP\n")
						name,score=quizgame("easy_kpop.txt",1)
						print()
						print(name,"scored:",score)
						print()

						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0
					
					elif category_choice==0:
						print("\nRETURNING TO MAIN MENU\n")
						difficulty_choice=0
					
					else:
						print("\nInvalid Choice!!\n")	
					
			elif difficulty_choice ==2:
				print("\nYou have chosen MEDIUM\nPlease choose a category\n")
				
				category_choice=None
				while category_choice != 0:
					category_choice=category_menu()
		
					if category_choice==1:
						un = os.system('cls')
						print("\nMEDIUM:Ultimate Frisbee\n")
						name,score=quizgame("medium_frisbee.txt",3)
						print()
						print(name,"scored:",score)
						print()
						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0
						
					elif category_choice==2:
						un = os.system('cls')
						print("\nMEDIUM:League of Legends\n")
						name,score=quizgame("medium_league.txt",3)
						print()
						print(name,"scored:",score)
						print()
						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0
						
					elif category_choice==3:
						un = os.system('cls')
						print("\nMEDIUM:KPOP\n")
						name,score=quizgame("medium_kpop.txt",3)
						print()
						print(name,"scored:",score)
						print()
						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0

					elif category_choice==0:
						print("\nRETURNING TO MAIN MENU\n")
						difficulty_choice=0
					
					else:
						print("\nInvalid Choice!!\n")

			elif difficulty_choice ==3:
				print("\nYou have chosen HARD\nPlease choose a category\n")
				
				category_choice=None
				while category_choice != 0:
					category_choice=category_menu()
		
					if category_choice==1:
						un = os.system('cls')
						print("\nHARD:Ultimate Frisbee\n")
						name,score=quizgame("hard_ultimate.txt",5)
						print(name,"scored:",score)
						print()
						
						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0

					elif category_choice==2:
						un = os.system('cls')
						print("\nHARD:League of Legends\n")
						name,score=quizgame("hard_league.txt",5)
						print(name,"scored:",score)
						print()
						
						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0

					elif category_choice==3:
						un = os.system('cls')
						print("\nHARD:KPOP\n")
						name,score=quizgame("hard_kpop.txt",5)
						print(name,"scored:",score)
						print()
						
						checked_list=name_check(highscore_list,name,score)
						highscore_list=selection_sort(checked_list)
						category_choice=0
						difficulty_choice=0

					elif category_choice==0:
						print("\nRETURNING TO MAIN MENU\n")
						difficulty_choice=0
					else:
						print("\nInvalid Choice!!\n")

			elif difficulty_choice==0:
				print("\nRETURNING TO MAIN MENU\n")
			else:					
				print("\nInvalid Choice!!\n")	

	#View High Scores (File open and read mode)
	elif choice==2:
		print("---------------------------")
		print("|    TOP 10 HIGHSCORES    |")
		print("---------------------------\n")
		
		highscore_list=selection_sort(highscore_list)

		if highscore_list==[[]]:
			print("\n - - - - - EMPTY - - - - - \n")
		elif highscore_list==[]:
			print("\n - - - - - EMPTY - - - - - \n")
		else:
			highscore_list=selection_sort(highscore_list)
			
			display=0
			if len(highscore_list)<10:
				while display!=len(highscore_list):
					print(highscore_list[display][0],highscore_list[display][1])
					display=display+1
			else:
				while display !=10:
					print(highscore_list[display][0],highscore_list[display][1])
					display=display+1
		print()
	
	elif choice==3:
		print("\nReset High Scores")
		highscore_list=[]
		fileSaver=open("highscore_roster.txt","w")
		fileSaver.write("")
		fileSaver.close()
		print("\nScores have been reset!!")
		print("\n- - HIGH SCORES NOW EMPTY - -\n")
	
	
	elif choice==0:
		fileSaver=open("highscore_roster.txt","w")
		for e in highscore_list:
			fileSaver.write(e[0]+","+str(e[1])+"\n")
		fileSaver.close()
		print("__________________________")
		print("|                        |")
		print("| THANK YOU FOR PLAYING! |")
		print("|________________________|\n")
		
	
	else:
		print("\n\nInvalid choice or Function not available!\n")
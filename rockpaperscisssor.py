"""
WORKFLOW OF PROJECT:
1- INPUT FROM USER(ROCK,PAPER,SCISSOR )
2- COMPUTER CHOICE 
3- RESULT PRINT 

CASES:
A- ROCK
ROCK-ROCK=TIE
ROCK-PAPER=PAPER WINS
ROCK-SCISSOR=ROCK WINS

B-PAPER
PAPER-ROCK=PAPER WINS
PAPER-SCISSOR=SCISSOR WINS
PAPER-PAPER=TIE

C-SCISSOR
SCISSOR-ROCK=ROCK WINS
SCISSOR-PAPER=SCISSOR WINS
SCISSSOR-SCISSOR=TIE

"""
import random
item_list = ["Rock","Paper","Scissor"]

user_choice =input("Enter your move= Rock,Paper,Scissor")
comp_choice =random.choice(item_list)

print(f"User choice ={user_choice}, Computer choice ={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same: = Match tie")

elif user_choice == "Rock":
 if comp_choice =="Paper":
    print("Paper covers Rock = Computer win")
 else:
    print("Rock smashes Scissor = you win")

elif user_choice == "Paper":
   if comp_choice == "Scissor":
    print("Scissor cuts Paper = computer win")
   else:
    print("Paper covers Rock = you win")

elif user_choice == "Scissor":
   if comp_choice == "Paper":
    print("Scissor cuts Paper = you win") 
   else:
     print("Rock smashes Scissor = computer win")     
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Welcome to the game of ROCK,PAPAER and SCISSORS.")
print("Get Ready.")
while True:
 user_choice=int(input("Enter \n1 - Rock\n2 - Paper\n3 - Scissor.\n"))
 if user_choice<1 or user_choice>3:
   print("You have typed n invalid number.")

  
 computer_choice=random.randint(1,3)

  
 if user_choice==computer_choice:
  if user_choice==1:
    if computer_choice==1:
      print("Your choice.")
      print("\n")
      print(rock)
      print("\n")
      print("Computer choice.")
      print(rock)
      print("Draw match.\n")

   
  elif user_choice==2:
    if computer_choice==2:
      print("Your choice.")
      print("\n")
      print(paper)
      print("\n")
      print("Computer choice.")
      print(paper)
      print("Draw match.\n")

   
  else:
    if computer_choice==3:
      print("Your choice.")
      print("\n")
      print(scissors)
      print("\n")
      print("Computer choice.")
      print(scissors)
      print("Draw match.\n")
      
  yes_no=input("Do you want to play again : Y or N\n")
  yes_no.lower()
  if yes_no=="N":
    break
  
 else:
  if user_choice==1:
    if computer_choice==2:
      print("your choice.\n")
      print(rock)
      print("\n")
      print("computer choice.")
      print(paper)
      print("You lost.")
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
        break
    else:
      print("your choice.\n")
      print(rock)
      print("\n")
      print("computer choice.")
      print(scissors)
      print("Huurrayyyyy you won!!!")
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
         break
  elif user_choice==2:
    if computer_choice==1:
      print("your choice.\n")
      print(paper)
      print("\n")
      print("computer choice.")
      print(rock)
      print("Huurrayyyyy you won!!!")
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
        break
    else:
      print("your choice.\n")
      print(paper)
      print("\n")
      print("computer choice.")
      print(scissors)
      print("You lost")
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
       break
      
      
  elif user_choice==3:
    if computer_choice==1:
      print("your choice.\n")
      print(scissors)
      print("\n")
      print("computer choice.")
      print(rock)
      print("You lost")
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
        break
    else: 
      print("your choice.\n")
      print(scissors)
      print("\n")
      print("computer choice.")
      print(paper)
      print("Huurrayyyyy you won!!!")
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
       break
  else:
      yes_no=input("Do you want to play again : Y or N\n")
      yes_no.lower()
      if yes_no=="N":
       break
    
      
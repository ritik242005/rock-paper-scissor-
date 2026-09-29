print("                                                              WELCOME TO ROCK PAPER SCISSORS!")
   


print("                                                             ================================")
print("                                                                Rock, Paper, Scissors Game")
print("                                                             ================================")




answer = input("Do you want to play the game? (yes/no): ")
if answer != "yes":
    print("Thanks for visiting, Goodbye!")
    exit()
    




import random
choices = ["rock", "paper", "scissors"]

user_score =0
computer_score =0

while user_score<3 and computer_score<3:



  users_choice = input("Enter your move = rock, paper, scissors=  ")
  comp_choice = random.choice(choices)



  print("Computer choosed: {comp_choice}")
  print("User choosed: {user_choice}")

  if users_choice == comp_choice :
    print("It's a tie! = both choosed the same")
  elif users_choice =="rock":
    if comp_choice =="paper":
        print("Paper covers Rock = computer wins")
        computer_score += 1
    else:
        print("Rock wins! =you win")
        user_score += 1

  elif users_choice =="paper":
    if comp_choice =="scissors":
        print("Scissors cuts Paper = computer wins")
        computer_score += 1
    else:
        print("Paper wins! =you win")
        user_score += 1

  elif users_choice =="scissors":
    if comp_choice =="rock":
        print("Rock crushes Scissors = computer wins")
        computer_score += 1
    else:
        print("Scissors wins! =you win")
        user_score += 1

  print("User Score:{user_score}")

  print("Computer Score:{computer_score}")


if user_score ==3:
 print("You won the game")
else:
 print("Computer won the game")


print(                                                        "Thanks for playing, Goodbye!")
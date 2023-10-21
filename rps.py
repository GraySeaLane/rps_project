# For this project, you and your partner(s) will work to create a program that has a "player" and a "computer" adversary. The computer should randomly choose its decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision. 


# If player and computer choose the same decision then display ("Game Tied"), 


# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and 
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") 
# -- Vice versa for other decisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").




# rock_paper()

# user_input = int(input("Welcome to Rock, Paper & Scissors! Input 0 for rock, 1 for paper and 2 for scissors. If you would like to quit please press 4."))
# comp_input = 

#     def rock = 0
#     def paper = 1
#     def scissors = 2
#     def quit = 4

# While true

#     if (user input is 2 and computer input is 1) or (user_input is 1 and comp_input is 0) or (user_input is 0 and comp_input is 2)
#         print("You Won! YAY!!")
#     elif:
#     (user input is 1 and computer input is 2) or (user_input is 0 and comp_input is 1) or (user_input is 2 and comp_input is 0)
#         print("You lost! Please try again!")
#     elif:
#         user_input == comp_input 
#          print("It's a tie")
#     else
#         user_input == 4
#         break
#         print("Thank you for playing.")


import random
def rock_paper():
    wins =0
    loses = 0
    ties = 0

    while True:
        user_input = int(input("Welcome to Rock, Paper & Scissors! Input 0 for rock, 1 for paper and 2 for scissors. If you would like to quit please press 4."))

        comp_input = random.choice([0,1,2])

        if user_input ==0:
            if comp_input ==0:
                print("tie")
                ties += 1
            elif comp_input ==1:
                print("lose")
                loses +=1
            else:
                print("win")
                wins +=1

        if user_input ==1:
            if comp_input ==0:
                print("win")
                wins +=1

            elif comp_input ==1:
                print("tie")
                ties += 1

            else:
                print("lose")
                loses +=1    
        
        if user_input ==2:
            if comp_input ==0:
                print("lose")
                loses +=1
            elif comp_input ==1:
                print("win")
                wins +=1

            else:
                print("tie")
                ties += 1

        if user_input ==4:
    
            print("Thank you for playing")
            print(f"The record is {wins} wins, {loses} loses, {ties}, ties")
            break

rock_paper()
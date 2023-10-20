# For this project, you and your partner(s) will work to create a program that has a "player" and a "computer" adversary. The computer should randomly choose its decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision. 


# If player and computer choose the same decision then display ("Game Tied"), 


# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and 
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") 
# -- Vice versa for other decisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").

cart = {}
while True: #this is going to run until i give it a break condition
    item = input("What would you like to add? ")
    print(item)
    quantity = int(input("How many would you like to add?"))
    print(quantity)
    
    if item not in cart:
        cart[item] = quantity
    else:
        cart[item] += quantity
    print(cart)
    
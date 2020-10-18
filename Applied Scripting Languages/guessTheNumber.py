# program to guess the number by A00206086

#import randit and create random number
from random import randint
rand_number = randint(1,30)
count = 0 # count number of guesses
game_over = False #is user finished playing

while game_over == False:
    guess = int(input("Enter a number between 1-30: ")) # users guess
    #Reached Max number of guesses for this game
    if(count > 10):
        print("You have guessed too many times")
        play_again = input("Do you want to play again? (y/n)")
        if play_again =='y':
            count = 0
            rand_number = randint(1,30) #as its going to be a new game create a new random number
        else:
            print("Game Over")
            game_over == True #end game/loop
    #User Guessed Correctly
    elif(guess == rand_number):
        print(f"You guessed correctly! random number was {rand_number}")
        play_again = input("Do you want to play again? (y/n)") #ask to play again
        if play_again =='y':
            count = 0 #reset counter
            rand_number = randint(1,30) #as its going to be a new game create a new random number
        else:
            print("Game Over")
            game_over = True #end game/loop
            break
    #User Guessed too low
    elif(guess < rand_number):
        count +=1
        print("Your guess was too low! Try Again!")
    #user guessed too high
    elif(guess > rand_number):
        count +=1
        print("Your guess was too high! Try Again")
    

    
        
    



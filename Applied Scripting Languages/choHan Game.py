#program to demonstate the ChoHanGame by A00206086
from random import randint
#input users guess (odd/even)
usersGuess = input("Enter your guess (odd or even): ")

#roll the dice
diceRoll1 = randint(1,6)
diceRoll2 = randint(1,6)
#get dice total
diceTotal = diceRoll1 + diceRoll2
#print dice results
print(f"Dice rolls: {diceRoll1} and {diceRoll2} Total is : {diceTotal}")

#check if odd and even
if diceTotal % 2 ==0 :
    result = "even"
else:
    result = "odd"
#Check if user is correct   
if usersGuess.lower() == result:
    print("You guessed correct")
else:
    print("You guessed wrong")

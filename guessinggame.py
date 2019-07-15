#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
tries=3
numberofguesses=0
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer
    numberofguesses+=1

while numberofguesses >0:
    if int(guess)!= aRandomNumber:
        tries-=1
        print ("Nope, try again")
        break
    elif int(guess)= aRandomNumber:
        print("Congratulations! You got it right!")
        break

if tries==0:
    print("You have no more tries sorry.")

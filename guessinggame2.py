#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
tries=0


while tries < 3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer


	if int(guess) == aRandomNumber:
		print ("Congratulations, you got it")
		break
	elif int(guess) > aRandomNumber:
		print ("try again, thats too high")
		break
	else
		print ("try again, thats too low")
		break
	tries+=1

print("Sorry, the number was") +str(aRandomNumber)

# coding: utf-8
'''
Python Die Roller Program by Nicholas Taylor
Remade Java Die Roller in Python to test functionality changes between the two languages
'''
import random

def main():
	print("DND Dice Roller :: Nicholas Taylor")
	print(":::::::::::::::::::::::::::::::::")
	AskForUserInput() # start of program functionality

def AskForUserInput():
	try:
		print() # blank line for looks
		dieAmount, dieSides = input("Die to be rolled (XdX)? ").split("d", 2) # dnd rolling effect split
		dieAmount = int(dieAmount)
		dieSides = int(dieSides)
		RollDieAndOutput(dieAmount, dieSides) # function to roll die
	except ValueError:
		print("!!! Please enter in proper format ex. 3d10 -> 3 10-sided dice !!!")
		AskForUserInput()

def RollDieAndOutput(dieAmount, dieSides):
	print()
	totalRoll = 0
	maxPossibility = dieAmount * dieSides # multiply to calculate best possible rolls
	print(f'Rolling {dieAmount}d{dieSides} with a max possibility of {maxPossibility}\n')
	for die in range(1, dieAmount+1): # loop to randomize die rolls
		dieRoll = random.randint(1, dieSides)
		totalRoll += dieRoll
		print(f'Die {die}: {dieRoll}')
	print('=====================')
	print(f'** Total Roll: {totalRoll} **\n')
	state = input('Would you like to roll same dice again (Y/N)? ') # prompt user to roll again or not
	if state == 'Y':
		RollDieAndOutput(dieAmount, dieSides) # if Y, reroll same dice
	else:
		AskForUserInput() # if anything but Y, reprompt user on dice to roll
	
main()

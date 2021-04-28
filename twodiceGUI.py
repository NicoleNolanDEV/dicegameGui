"""
Program: twodiceGUI.py
Author: Nicole Nolan 04/28/21

*** Note: the file breezypythongui.py MUST be in the same directory as this file for the application to work. In addition, you MUST install the pygame package by runing: pip install pygame. Please be sure to have the associated MP3 files in the appropriate repository ***
"""

from breezypythongui import EasyFrame
from pygame import mixer
import random



class DiceGame(EasyFrame):
	

	def __init__(self):
		
		EasyFrame.__init__(self, title = "Roll the Dice!", resizable = False, background = "lightgreen")

		self.addLabel(text = "Let's Play a Game", row = 0, column = 0, columnspan = 3, sticky = "NSEW", background = "lightgreen").config(font = ("Courier", 30, "bold"))
		self.player = self.addIntegerField(value = 0, row = 2, column = 0, sticky = "NSEW", state = "readonly")
		self.player.config(font = ("Courier", 12))
		self.addLabel(text = "  Your Die  ", row = 1, column = 0, sticky = "NSEW", background = "lightgreen").config(font = ("Courier", 15))
		self.computer = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NSEW", state = "readonly")
		self.computer.config(font = ("Courier", 12))
		self.addLabel(text = "Computer Die", row = 1, column = 1, sticky = "NSEW", background = "lightgreen").config(font = ("Courier", 15))
		self.button = self.addButton(text = "ROLL", row = 3, column = 0, columnspan = 3, command = self.roll).config(font = ("Courier", 10, "bold"))
		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 3, sticky = "NSEW")
		self.resultArea.config(font = ("Courier", 20, "bold"))

	def roll(self):
		
		playerRoll = random.randint(1, 6)
		computerRoll = random.randint(1, 6)
		result = ""

		if playerRoll > computerRoll:
			result = "You WIN!"
			file = "applause.mp3"
			mixer.init()
			mixer.music.load(file)
			mixer.music.play()

		elif computerRoll > playerRoll:
			result = "The Computer Wins!"
			file = "boo.mp3"
			mixer.init()
			mixer.music.load(file)
			mixer.music.play()

		else:
			result = "It's a tie! Roll Again!"
			file = "diceRoll.mp3"
			mixer.init()
			mixer.music.load(file)
			mixer.music.play()
			#points -= 10


		self.player.setNumber(playerRoll)
		self.computer.setNumber(computerRoll)
		self.resultArea["text"] = result

def main():
	DiceGame().mainloop()

main()
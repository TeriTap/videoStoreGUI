"""
Program: videoStoreGUI.py
Author: Teri  07.18.23

GUI-based version of the video store project from Chapter 2

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (application name will change project to project)
class VideoStoreGUI(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		# Call to the Easy Frame constructor method
		EasyFrame.__init__(self, title = "Five Star Video", width = 350, height = 290, resizable = False, background = "skyblue")
		self.normalFont = Font(family = "Verdana", size = 16)

		# Add the various components to the window
		self.addLabel(text = "Five Star Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "black", foreground = "skyblue", font = Font(family = "Impact", size = 26))
		self.addLabel(text = "**Video Rental Prices**\nNew Rentals - $3.00\nOld Rentals - $2.00", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "skyblue", foreground = "magenta", font = self.normalFont)
		self.addLabel(text = "# of New Rentals: ", row = 2, column = 0, sticky = "NE", background = "skyblue", foreground = "magenta", font = self.normalFont)
		self.newRentals = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NW", width = 4)
		self.addLabel(text = "# of Old Rentals: ", row = 3, column = 0, sticky = "NE", background = "skyblue", foreground = "magenta", font = self.normalFont)
		self.oldRentals = self.addIntegerField(value = 0, row = 3, column = 1, sticky = "NW", width = 4)

		self.button = self.addButton(text = "Check Out", row =  4, column = 0, columnspan = 2, command = self.calculate)

		self.addLabel(text = "Order Summary: ", row = 5, column = 0, sticky = "NE", background = "skyblue", foreground = "magenta", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 6)

	# Definition of the calculate() function
	def calculate(self):
		# Grab the user input from the GUI window
		new = self.newRentals.getNumber()
		old = self.oldRentals.getNumber()

		# Processing phase
		result = (new * 3.0) + (old * 2.0)

		# Output phase
		self.total.setNumber(result)

# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	VideoStoreGUI().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()
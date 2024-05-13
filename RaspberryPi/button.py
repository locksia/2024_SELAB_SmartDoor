from gpiozero import Button
from time import sleep

pushButton = Button(20)

class JudegementDoorlockUsed:
	def __init__(self):
		self.isDoorlockUsed = False
	
	def SetIsDoorlockUsed(self):
		self.isDoorlockUsed = pushButton.is_pressed
	
	def GetIsDoorlockUsed(self):
		return self.isDoorlockUsed
		

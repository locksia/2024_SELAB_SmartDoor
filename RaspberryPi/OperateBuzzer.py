from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

class OperateBuzzer:
	def __init__(self):
		#self.buzzerDeviceStatus = False
		self.isDoorForcedOpend = False
	
	def SetBuzzerDeviceStatus(self, isDoorForcedOpend):
		if(isDoorForcedOpend == True):
			buzzer.on()
		else :
			buzzer.off()
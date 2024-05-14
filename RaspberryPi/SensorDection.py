from gpiozero import MotionSensor
from gpiozero import DistanceSensor
from time import sleep

ultraSonic = DistanceSensor(echo=23, trigger=24)
InfraredSensorDetected = MotionSensor(21)

class SensorDetection():
	def __init__(self):
		self.detectionReferenceTime = 0
		self.isUltrasonicSensorDetected = False #DoorOpend
		self.isInfraredSensorDetected = False
		self.isDoorlockUsed = False
		self.isHumanDetected = False
		self.isDoorForcedOpend = False
		self.isDoorNormallyOpend = False
		
	#[small_function] humandetected
	def SetIsfraredSensorDetected(self):
		self.isInfraredSensorDetected = InfraredSensorDetected.value
		
	def GetIsfraredSensorDetected(self):
		return self.isInfraredSensorDetected
		
	def SetIsHumandetected(self, isInfraredSensorDetected, detectionReferenceTime):
		if(isInfraredSensorDetected == True):# Need to add about detcetionReferenceTime
			self.isHumanDetected = True
		else:
			self.isHumanDetected = False
	
	def GetIsHumandetected(self):
		return self.isHumanDetected

	#[small_function] doorforcedopend
	def SetIsUltrasonicSensorDetected(self):
		if(ultraSonic.distance > 0.1) : 
			self.isUltrasonicSensorDetected = True
		else : 
			self.isUltrasonicSensorDetected = False
	
	def GetIsUltrasonicSensorDetected(self):
		return self.isUltrasonicSensorDetected
	
	def SetIsDoorForcedOpend(self, isUltrasonicSensorDetected, isDoorlockUsed):
		if(isUltrasonicSensorDetected == True and isDoorlockUsed == False):
			self.isDoorForcedOpend = True
		else : 
			self.isDoorForcedOpend = False
	
	def GetIsDoorForcedOpend(self):
		return self.isDoorForcedOpend
	
	#[small_function] doornormallyopened
	def SetIsDoorNormallyOpend(self, isUltrasonicSensorDetected, isDoorlockUsed):
		if(isUltrasonicSensorDetected == True and isDoorlockUsed == True):
			self.isDoorNormallyOpend = True
		else : 
			self.isDoorNormallyOpend = False
	
	def GetIsDoorNormallyOpend(self):
		return self.isDoorNormallyOpend

from gpiozero import MotionSensor
from gpiozero import DistanceSensor
from time import sleep

ultraSonic = DistanceSensor(echo=23, trigger=24)
InfraredSensorDetected = MotionSensor(21)

class SensorDetection():
	def __init__(self):
		self.detectionReferenceCount = 0
		self.detectionCount = [0]
		self.isUltrasonicSensorDetected = False #DoorOpend
		self.isInfraredSensorDetected = False	#HumanDetected
		self.isDoorlockUsed = False
		self.isHumanDetected = False
		self.isDoorForcedOpend = False
		self.isDoorNormallyOpend = False
		
	#[small_function] humandetected
	def SetIsfraredSensorDetected(self):
		self.isInfraredSensorDetected = InfraredSensorDetected.value
		if(self.isInfraredSensorDetected == 1):
			self.isInfraredSensorDetected = True
		else:
			self.isInfraredSensorDetected = False
		
	def GetIsfraredSensorDetected(self):
		return self.isInfraredSensorDetected
		
	def SetIsHumandetected(self, isInfraredSensorDetected, detectionReferenceCount):
		if(isInfraredSensorDetected == True):
			self.detectionCount.append(1)
		else:
			self.detectionCount.append(0)
		
		if(len(self.detectionCount) > 10):#Test Required
			self.detectionCount.clear()
			if(isInfraredSensorDetected == True):
				self.detectionCount.append(1)
			else:
				self.detectionCount.append(0)
			
		else:
			if sum(self.detectionCount) > detectionReferenceCount:
				self.isHumanDetected = True
			else:
				self.isHumanDetected = False
	
	def GetIsHumandetected(self):
		return self.isHumanDetected

	#[small_function] ultrasonicsensor
	def SetIsUltrasonicSensorDetected(self):
		if(ultraSonic.distance > 0.1) : 
			self.isUltrasonicSensorDetected = True
		else : 
			self.isUltrasonicSensorDetected = False
	
	def GetIsUltrasonicSensorDetected(self):
		return self.isUltrasonicSensorDetected
	
	#[small_function] doorforcedopened
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
		
if __name__ == '__main__':
	SensorDetection = SensorDetection()
	ultrasonic = True
	isdoorlock = True
	SensorDetection.SetIsDoorNormallyOpend(ultrasonic,isdoorlock)
	a = SensorDetection.GetIsDoorNormallyOpend()
	print('isdoornormallyopend : ',a)

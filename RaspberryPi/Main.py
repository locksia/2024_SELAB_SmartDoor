from Sensor import *
from buzzer import *
from button import *
from RecordCamera import *
from time import sleep

#GitTest
if __name__ == '__main__':
	#Object Declare
	SensorDetection = SensorDetection()
	OperateBuzzer = OperateBuzzer()
	JudegementDoorlockUsed = JudegementDoorlockUsed()
	RecordCamera = RecordCamera()
		
	#Var Declare
	detectionReferenceTime = 0
	isUltrasonicSensorDetected = 0.0
	isInfraredSensorDetected = False
	isDoorlockUsed = False
	isHumanDetected = False
	isDoorForcedOpend = False
	isDoorNormallyOpend = False
	
	#~~~
	print("--------------------------------------------------")
	while True:
		sleep(0.2)
		SensorDetection.SetIsfraredSensorDetected()
		SensorDetection.SetIsUltrasonicSensorDetected()
		JudegementDoorlockUsed.SetIsDoorlockUsed()
		
		isInfraredSensorDetected = SensorDetection.GetIsfraredSensorDetected()
		isUltrasonicSensorDetected = SensorDetection.GetIsUltrasonicSensorDetected()
		isDoorlockUsed = JudegementDoorlockUsed.GetIsDoorlockUsed()
		
		SensorDetection.SetIsDoorForcedOpend(isUltrasonicSensorDetected, isDoorlockUsed)
		isDoorForcedOpend = SensorDetection.GetIsDoorForcedOpend()
		
		
		print("motion detect : ",isInfraredSensorDetected)
		print("distance : ",isUltrasonicSensorDetected)
		print("doorlockused : ", isDoorlockUsed)
		OperateBuzzer.SetBuzzerDeviceStatus(isDoorForcedOpend)
		RecordCamera.SetRecordCamera(isDoorForcedOpend)
		
		print("--------------------------------------------------")
		sleep(1.0)

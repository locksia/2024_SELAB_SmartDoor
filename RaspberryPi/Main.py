#Import classes from py source code
from SensorDection import *
from OperateBuzzer import *
from JudgementDoorlockUsed import *
from RecordCamera import *
from StreamingCamera import *
from RecordEntryTime import *

from time import sleep

if __name__ == '__main__':
	#Declare objects
	SensorDetection = SensorDetection()
	OperateBuzzer = OperateBuzzer()
	JudegementDoorlockUsed = JudegementDoorlockUsed()
	RecordCamera = RecordCamera()
	StreamingCamera = StreamingCamera()
	RecordEntryTime = RecordEntryTime()

	#Declare vars
	detectionReferenceCount = 10
	isUltrasonicSensorDetected = False
	isInfraredSensorDetected = False
	isDoorlockUsed = False
	isHumanDetected = False
	isDoorForcedOpend = False
	isDoorNormallyOpend = False
	
	#Loop
	print("--------------------------------------------------")
	while True:
		sleep(0.2)

		#Sensor Detection
		SensorDetection.SetIsfraredSensorDetected()
		SensorDetection.SetIsUltrasonicSensorDetected()	#Door
		JudegementDoorlockUsed.SetIsDoorlockUsed() #Doorlock Button
		
		#Assign Sensor Value
		isInfraredSensorDetected = SensorDetection.GetIsfraredSensorDetected()
		isUltrasonicSensorDetected = SensorDetection.GetIsUltrasonicSensorDetected()
		isDoorlockUsed = JudegementDoorlockUsed.GetIsDoorlockUsed()
		
		#SensorDetction - IsDoorForcedOpend, IsDoorNomallyOpend, HumanDetected
		SensorDetection.SetIsDoorForcedOpend(isUltrasonicSensorDetected, isDoorlockUsed)
		isDoorForcedOpend = SensorDetection.GetIsDoorForcedOpend()
		SensorDetection.SetIsDoorNormallyOpend(isUltrasonicSensorDetected, isDoorlockUsed)
		isDoorForcedOpend = SensorDetection.GetIsDoorNormallyOpend()
		SensorDetection.SetIsHumandetected(isInfraredSensorDetected, detectionReferenceCount)
		isHumanDetected = SensorDetection.GetIsHumandetected()

		#OperateBuzzer
		OperateBuzzer.SetBuzzerDeviceStatus(isDoorForcedOpend)
		
		#RecordCamera
		RecordCamera.SetRecordCamera(isDoorForcedOpend, isHumanDetected)

		#RecordEntryTime
		RecordEntryTime.SetDetectedTime(isDoorNormallyOpend)
		detectionReferenceTime = RecordEntryTime.GetDetectedTime()
	
		#Send Data To DB

		print("motion detect : ",isInfraredSensorDetected)
		print("distance : ",isUltrasonicSensorDetected)
		print("doorlockused : ", isDoorlockUsed)
		OperateBuzzer.SetBuzzerDeviceStatus(isDoorForcedOpend)
		RecordCamera.SetRecordCamera(isDoorForcedOpend)
		
		print("--------------------------------------------------")
		sleep(1.0)

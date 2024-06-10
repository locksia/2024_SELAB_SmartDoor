#Import classes from py source code
from SensorDection import *
from OperateBuzzer import *
from JudgementDoorlockUsed import *
from RecordCamera import *
from StreamingCamera import *
from RecordEntryTime import *
from DB import *

import threading

from time import sleep

if __name__ == '__main__':
	#Declare objects
	SensorDetection = SensorDetection()
	OperateBuzzer = OperateBuzzer()
	JudegementDoorlockUsed = JudegementDoorlockUsed()
	RecordCamera = RecordCamera()
	RecordEntryTime = RecordEntryTime()
	SendDataToDB = SendDataToDB()

	#Declare vars
	detectionReferenceCount = 2
	detectedTime = "0" #When door normally opened
	isUltrasonicSensorDetected = False
	isInfraredSensorDetected = False
	isDoorlockUsed = False
	isHumanDetected = False
	isDoorForcedOpend = False
	isDoorNormallyOpend = False
		
	def basic() :
		while True:
			sleep(0.5)
			#Sensor Detection
			SensorDetection.SetIsfraredSensorDetected()
			SensorDetection.SetIsUltrasonicSensorDetected()	#Door Opend
			JudegementDoorlockUsed.SetIsDoorlockUsed() #Doorlock Button
			
			#Assign Sensor Value
			isInfraredSensorDetected = SensorDetection.GetIsfraredSensorDetected()
			isUltrasonicSensorDetected = SensorDetection.GetIsUltrasonicSensorDetected()
			isDoorlockUsed = JudegementDoorlockUsed.GetIsDoorlockUsed()
			
			#SensorDetction - IsDoorForcedOpend, IsDoorNomallyOpend, HumanDetected
			SensorDetection.SetIsDoorForcedOpend(isUltrasonicSensorDetected, isDoorlockUsed)
			isDoorForcedOpend = SensorDetection.GetIsDoorForcedOpend()		
			SensorDetection.SetIsDoorNormallyOpend(isUltrasonicSensorDetected, isDoorlockUsed)
			isDoorNormallyOpend = SensorDetection.GetIsDoorNormallyOpend()
			SensorDetection.SetIsHumandetected(isInfraredSensorDetected, detectionReferenceCount)
			isHumanDetected = SensorDetection.GetIsHumandetected()
			
			#OperateBuzzer
			OperateBuzzer.SetBuzzerDeviceStatus(isDoorForcedOpend)
			
			#RecordCamera
			RecordCamera.SetRecordCamera(isDoorForcedOpend, isHumanDetected)

			#RecordEntryTime
			RecordEntryTime.SetDetectedTime(isDoorNormallyOpend)
			detectedTime = RecordEntryTime.GetDetectedTime()
			
			#Send Data To DB
			SendDataToDB.SetData(isHumanDetected,isDoorForcedOpend,detectedTime)
			SendDataToDB.SendAlarmDataToDB()
			SendDataToDB.SendDetetcedTime()		
			
			print("--------------------------------------------------")
			print("isInfraredSensorDetected : ",isInfraredSensorDetected)
			print("isUltrasonicSensorDetected : ",isUltrasonicSensorDetected)
			print("isDoorlockUsed : ",isDoorlockUsed)
			
			print("isHumanDetected : ",isHumanDetected)
			print("isDoorForcedOpend : ",isDoorForcedOpend)
			print("isDoorNormallyOpend : ",isDoorNormallyOpend)
			
			print("detectionCount : ", SensorDetection.detectionCount)
			
			print("detectedTime : ", detectedTime)
			
			print("--------------------------------------------------")
	
	servo_thread1 = threading.Thread(target = basic)
	servo_thread1.start()

	StreamingCamera()
	
	

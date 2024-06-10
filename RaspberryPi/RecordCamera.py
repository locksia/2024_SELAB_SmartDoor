from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import Transform

import time
from DB import *

picam2 = Picamera2(1)
video_config = picam2.create_video_configuration(transform=Transform(hflip=True, vflip=True))
picam2.configure(video_config)

db = pymysql.connect(host='220.69.240.117', port=3306, user='SeRas', passwd='selab', db='smartdoor', charset='utf8')
curs = db.cursor()

class RecordCamera():
	def __init__(self):
		self.recordCamera = False
		self.isHumanDetected = False
		self.isDoorForcedOpend = False
		
	def SetRecordCamera(self, isDoorForcedOpend, isHumanDetected):
		if(isDoorForcedOpend == True or isHumanDetected == True):
			encoder = H264Encoder(1000000)
			recordedTime = time.strftime('%Y_%m_%d-%H:%M:%S') + ".mp4"			
			
			output = FfmpegOutput(recordedTime, audio=True)

			picam2.start_recording(encoder, output)
			time.sleep(5)
			picam2.stop_recording()
			time.sleep(1)
			#Send mp4 to DB
			print("Start Send mp4")
			with open(recordedTime, 'rb') as f:
				binary_data = f.read()
			print("Binary Data readed")
			sql = 'INSERT INTO raspi_recordedvideos (recordedVideo, recordedTime) VALUES(%s, %s)'
			curs.execute(sql, (binary_data, recordedTime))
			db.commit()
			
if __name__ == "__main__":
	RecordCamera = RecordCamera()
	RecordCamera.SetRecordCamera(True, True)
	

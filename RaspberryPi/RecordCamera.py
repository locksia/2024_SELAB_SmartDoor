from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

class RecordCamera():
	def __init__(self):
		self.recordCamera = False
		self.isHumanDetected = False
		self.isDoorForcedOpend = False
		
	def SetRecordCamera(self, isDoorForcedOpend, isHumanDetected):
		if(isDoorForcedOpend == True or isHumanDetected == True):
			encoder = H264Encoder(1000000)
			RecordedTime = time.strftime('%Y_%m_%d-%H:%M:%S') + ".mp4"
			
			
			output = FfmpegOutput(RecordedTime, audio=True)

			picam2.start_recording(encoder, output)
			time.sleep(10)
			picam2.stop_recording()
			#Send mp4 to DB

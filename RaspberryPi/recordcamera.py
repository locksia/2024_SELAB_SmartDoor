from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

import time
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
#asd
class RecordCamera():
	def __init__(self):
		self.recordCamera = False
		self.isHumanDetected = False
		self.isDoorForcedOpend = False
		self.recordVideoUrl = ""
		
	def SetRecordCamera(self, isDoorForcedOpend):
		if(isDoorForcedOpend == True):
			encoder = H264Encoder(1000000)
			output = FfmpegOutput('test.mp4', audio=True)

			picam2.start_recording(encoder, output)
			time.sleep(10)
			picam2.stop_recording()
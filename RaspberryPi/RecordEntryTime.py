import time

class RecordEntryTime():
    def __init__(self):
        self.isDoorNormallyOpend = False
        self.detectedTime = 0
    
    def SetDetectedTime(self, isDoorNormallyOpend):
        if isDoorNormallyOpend == True:
            self.detectedTime = time.strftime('%Y.%m.%d - %H:%M:%S')
        else:
            self.detectedTime = 0

    def GetDetectedTime(self):
        return self.detectedTime
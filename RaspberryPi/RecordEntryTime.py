import time

class RecordEntryTime():
    def __init__(self):
        self.isDoorNormallyOpend = False
        self.detectedTime = 0
    
    def SetDetectedTime(self, isDoorNormallyOpend):
        self.isDoorNormallyOpend = isDoorNormallyOpend
        if self.isDoorNormallyOpend == True:
            self.detectedTime = time.strftime('%Y.%m.%d - %H:%M:%S')
        else:
            self.detectedTime = 0

    def GetDetectedTime(self):
        return self.detectedTime
        
if __name__ == '__main__':
    a = time.strftime('%Y.%m.%d - %H:%M:%S') + ".mp4"
    print(type(a))

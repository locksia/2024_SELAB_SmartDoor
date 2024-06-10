import pymysql
import time

db = pymysql.connect(host='220.69.240.117', port=3306, user='SeRas', passwd='selab', db='smartdoor', charset='utf8')
curs = db.cursor()

class SendDataToDB():
    def __init__(self):
        self.isHumanDetected = False
        self.isDoorForcedOpend = False
        self.detectedTime = "0"
                
    def SetData(self, isHumanDetected, isDoorForcedOpend, detectedTime):
        self.isHumanDetected = isHumanDetected
        self.isDoorForcedOpend = isDoorForcedOpend
        self.detectedTime = detectedTime
        
    def SendAlarmDataToDB(self):
            if(self.isHumanDetected == True or self.isDoorForcedOpend == True):
                sql = 'INSERT INTO raspi_alarm (isHumanDetected, isDoorForcedOpened) VALUES(%r, %r)'
                curs.execute(sql, (self.isHumanDetected, self.isDoorForcedOpend))
                db.commit()
                time.sleep(5)
                self.isHumanDetected = False
                self.isDoorForcedOpend = False
                sql = 'INSERT INTO raspi_alarm (isHumanDetected, isDoorForcedOpened) VALUES(%r, %r)'
                curs.execute(sql, (self.isHumanDetected, self.isDoorForcedOpend))
                db.commit()
                
    def SendDetetcedTime(self):
        if self.detectedTime != "0":
                sql = 'INSERT INTO raspi_entrytime (entryTime) VALUES(%s)'
                curs.execute(sql, (self.detectedTime))
                db.commit()
        
    def SendRecordVieoToDB(self):
        sql = 'INSERT INTO raspi_recordedvideos (recordedVideo, recordedTime) VALUES(%s, %s)'
        curs.execute(sql, self.mp4Loc, self.recordedTime)
        db.commit()
                
if __name__ == '__main__':
        SendDataToDB = SendDataToDB()
        SendDataToDB.SetData(True,True,"1234-12-12-24-24-24")
        SendDataToDB.SendAlarmDataToDB()
        SendDataToDB.SendDetetcedTime()
        SendDataToDB.SetData(False,True,"1234-12-12-24-24-24")
        SendDataToDB.SendAlarmDataToDB()
        SendDataToDB.SendDetetcedTime()
        SendDataToDB.SetData(True,False,"1234-12-12-24-24-24")
        SendDataToDB.SendAlarmDataToDB()
        SendDataToDB.SendDetetcedTime()
        SendDataToDB.SetData(False,False,"1234-12-12-24-24-24")
        SendDataToDB.SendAlarmDataToDB()
        SendDataToDB.SendDetetcedTime()
        SendDataToDB.SetData(False,False,"0")
        SendDataToDB.SendAlarmDataToDB()
        SendDataToDB.SendDetetcedTime()

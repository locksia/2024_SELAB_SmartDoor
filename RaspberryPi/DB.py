import pymysql

db = pymysql.connect(host='220.69.240.117', port=3306, user='SeRas', passwd='selab', db='smartdoor', charset='utf8')
curs = db.cursor()

class SendDataToDB():
    def __init__():
        self.isHumanDetected = False
        self.isDoorForcedOpend = False
        self.detectedTime = 0
        self.mp4Loc = 0
                
    def SetData(self, isHumanDetected, isDoorForcedOpend, detectedTime, mp4Loc):
        self.isHumanDetected = isHumanDetected
        self.isDoorForcedOpend = isDoorForcedOpend
        self.detectedTime = detectedTime
        self.mp4Loc = mp4Loc
        
    def SendAlarmDataToDB(self):
        sql = 'INSERT INTO raspi_alarm (isHumanDetected, isDoorForcedOpened) VALUES(%r, %r)'
        curs.execute(sql, (self.isHumanDetected, self.isDoorForcedOpend))
        db.commit()
                
    def SendDetetcedTime(self):
        sql = 'INSERT INTO raspi_entrytime (entryTime) VALUES(%s)'
        curs.execute(sql, (self.detectedTime))
        db.commit()
        
    def SendRecordVieoToDB(self):
        print("Hello")
                
if __name__ == '__main__':
        sql = 'INSERT INTO raspi_alarm (isHumanDetected, isDoorForcedOpened) VALUES(%s, %s)'
        curs.execute(sql, (True, False))
        db.commit()

import pymysql

db = pymysql.connect(host='', port=, user='', passwd='', db='', charset='utf8')
curs = db.cursor()

class SendDataToDB():
    def __init__(self):
        self.isHumanDetected = False
        self.isDoorForcedOpend = False
        self.detectedTime = 0
                
    def SetData(self, isHumanDetected, isDoorForcedOpend, detectedTime):
        self.isHumanDetected = isHumanDetected
        self.isDoorForcedOpend = isDoorForcedOpend
        self.detectedTime = detectedTime
        
    def SendAlarmDataToDB(self):
        sql = 'INSERT INTO raspi_alarm (isHumanDetected, isDoorForcedOpened) VALUES(%r, %r)'
        curs.execute(sql, (self.isHumanDetected, self.isDoorForcedOpend))
        db.commit()
                
    def SendDetetcedTime(self):
        sql = 'INSERT INTO raspi_entrytime (entryTime) VALUES(%s)'
        curs.execute(sql, (self.detectedTime))
        db.commit()
        
    def SendRecordVieoToDB(self):
        sql = 'INSERT INTO raspi_recordedvideos (recordedVideo, recordedTime) VALUES(%s, %s)'
        curs.execute(sql, self.mp4Loc, self.recordedTime)
        db.commit()
                
if __name__ == '__main__':
        sql = 'INSERT INTO raspi_alarm (isHumanDetected, isDoorForcedOpened) VALUES(%s, %s)'
        curs.execute(sql, (True, False))
        db.commit()

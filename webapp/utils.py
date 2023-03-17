from datetime import date, datetime

def timeChange(startTime):
    currTime = datetime.now()
    convertedTime  = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S.%f')
    timePassed = currTime - convertedTime
    timePassedS = timePassed.seconds

    return timePassedS
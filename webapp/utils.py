from datetime import date, datetime

def timeChange(startTime):
    currTime = datetime.now()
    convertedTime  = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S.%f')
    timePassed = currTime - convertedTime
    timePassedS = timePassed.seconds

    return timePassedS


def newPointsLogic(hintsUsed, userTime, totalPoints):
    basePoints = 50
    #timeTaken = timeChange(userTime)
    timeTaken = userTime
    penalty = 0
    if(timeTaken > 300 or timeTaken < 1200):
         penalty += 10
    elif (timeTaken > 1200):
        penalty += 20
    if(hintsUsed == 1):
            penalty += 10
    elif(hintsUsed >= 2):
        penalty += 20

    basePoints -= penalty

    newPoints = totalPoints + basePoints
    print(newPoints)
    return(newPoints)

newPointsLogic(1, 900, 0)
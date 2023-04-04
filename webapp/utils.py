from datetime import date, datetime
from . import db
from flask_login import current_user
from .models import users, phone_challenge, laptop_challenge, server_challenge, points, splunk_challenges


def timeChange(startTime):
    currTime = datetime.now()
    convertedTime  = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S.%f')
    timePassed = currTime - convertedTime
    timePassedS = timePassed.seconds

    return timePassedS



def pointsLogic(challenge):
    

    hintsUsed = db.session.query(challenge.hints).filter_by(user_id = current_user.id).first()
    time = db.session.query(challenge.startTime).filter_by(user_id = current_user.id).first()
    totalPoints= db.session.query(points.pointsTotal).filter_by(id = current_user.id).first() 
    
    basePoints = 50
    #timeTaken = timeChange(userTime)
    timeTaken = timeChange(time[0])
    penalty = 0
    
    if(timeTaken > 300 and timeTaken < 1200):
         penalty += 10
    elif (timeTaken > 1200):
        penalty += 20
    if(hintsUsed[0] == 1):
            penalty += 10
    elif(hintsUsed[0] >= 2):
        penalty += 20

    basePoints -= penalty

    newPoints = totalPoints[0] + basePoints
    return(newPoints)


def splunk_markup(key):
    key_0 = '<div class = "splunk_instructions"><div class="locked">You have not unlocked the necessary flags to complete Splunk challenges, return to the evidence and obtain the flags required</div></div>'
    key_1 ='<div class="splunk_instructions"><div class="link">Follow this link to access the splunk server: <a href="http://52.1.222.178:8000" target="_blank">http://52.1.222.178:8000</a></div><div class="username">Username: ctf</div><div class="password">Password: EscapeEscap3</div><div class="setUp"><p>To set up your splunk follow these instructions</p><ul class="splunk_points"><li>Once logged in click search & report</li><li>Enter: source="ctf_dataset.log"</li><li>Change "last 24 hours" to "All time" on search bar</li><li>Use the flag from the previous question to search and answer the question</li><li>With the correct answer you will unlock a set of digits</li><li>Use these three sets of digits to escape the room</li></ul></div></div>'
    challenge_1 = '<div class="splunk_challenges"><h2>Splunk Challenges</h2><div class="splunk_challenge"><form action="" method="post" class="splunk_form"> <label for="challenge_one">1. How many log entries are there for the malicious actor\'s IP address?</label><input type="text" name="challenge_one" id="challenge_one"><input type = "submit" name = "challange_1" value = "Validate"></form><div></div></div>'
    challenge_1_c = '<div class="splunk_challenges"><h2>Splunk Challenges</h2><div class="splunk_challenge"><div>1. How many log entries are there for the malicious actor\'s IP address?</div><div> Answer: 17</div><div class="digits">Key: '
    challenge_2 = '<div class="splunk_challenge"><form action="" method="post" class="splunk_form"><label for="challenge_two">2. What common sql injection was entered into the password field by the malicious actor?</label><input type="text" name="challenge_two" id="challenge_two" placeholder="pass = \' or"><input type = "submit" name = "challange_2" value = "Validate"></form></div></div>'
    challenge_2_c = '<div class="splunk_challenge"><div>2. What common sql injection was entered into the password field by the malicious actor??</div><div>Answer: 1=1-- </div><div class="digits">Key: '
    challenge_3 = '<div class="splunk_challenge"><form action="" method="post" class="splunk_form"> <label for="challenge_three">3. Which plug-in was installed and activated by the malicious actor?</label><input type="text" name="challenge_three" id="challenge_three"><input type = "submit" name = "challange_2" value = "Validate"></form></div>'
    challenge_3_c = '<div class="splunk_challenge"><div>3. Which plug-in was installed and activated by the malicious actor?</div><div>Answer: File-manager</div><div class="digits">Key: 11</div></div>'

    splunkDigitOne = db.session.query(splunk_challenges.key_one).filter_by(user_id = current_user.id).first()
    splunkDigitTwo = db.session.query(splunk_challenges.key_two).filter_by(user_id = current_user.id).first()
    digitOne = str(splunkDigitOne[0])
    digitTwo = str(splunkDigitTwo[0])
    if key == 0:
        return key_0
    elif key == 1:
        key_1 += challenge_1
        return key_1
    elif key == 2:
        
        digits = str(splunkDigitOne[0])
        digitString = digits + '</div></div></div>'
        key_1 += challenge_1_c 
        key_1 += digitString
        return key_1
    elif key == 3:
        if splunkDigitOne[0] > 1:
            digits = str(splunkDigitOne[0])
            key_1 += challenge_1_c
            digitString = digits + '</div></div>'
            key_1 += digitString
            key_1 += challenge_2
            return key_1
        else:
            key_1 += challenge_1
            key_1 += challenge_2
            return key_1
    elif key == 4:
        if splunkDigitOne[0] > 1:
            key_1 += challenge_1_c
            digitOneStr = digitOne + '</div></div>'
            key_1 += digitOneStr
            key_1 += challenge_2_c
            digitTwoStr = digitTwo + '</div></div>'
            key_1 += digitTwoStr
            return key_1
        else: 
            key_1 += challenge_1
            key_1 += challenge_2_c
            key_1 += digitTwo
            return key_1
    elif key == 5:
        if splunkDigitOne[0] > 1 and splunkDigitTwo[0] > 1:
            key_1 += challenge_1_c
            key_1 += digitOne
            key_1 += challenge_2_c
            key_1 += digitTwo
            key_1 += challenge_3
            return key_1
        elif splunkDigitOne[0] > 1:
            key_1 += challenge_1_c
            key_1 += digitOne
            key_1 += challenge_2
            key_1 += challenge_3
            return key_1
        elif splunkDigitTwo[0] > 1:
            key_1 += challenge_1
            key_1 += challenge_2_c
            key_1 += digitTwo
            key_1 += challenge_3
            return key_1
    elif key == 6:
        if splunkDigitOne[0] > 1 and splunkDigitTwo[0] > 1:
            key_1 += challenge_1_c
            key_1 += digitOne
            key_1 += challenge_2_c
            key_1 += digitTwo
            key_1 += challenge_3_c
            return key_1
        elif splunkDigitOne[0] > 1:
            key_1 += challenge_1_c
            key_1 += digitOne
            key_1 += challenge_2
            key_1 += challenge_3_c
            return key_1
        elif splunkDigitTwo[0] > 1:
            key_1 += challenge_1
            key_1 += challenge_2_c
            key_1 += digitTwo
            key_1 += challenge_3_c
            return key_1
        






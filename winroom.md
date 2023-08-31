So here are the changes for the win room. It uses the splunk_challenges.key_one, two three etc to handle the changing of the locks. Basically if key_one isn't 0 then we set chall1 to complete. It passes these into cyberescape.html which then changes the background images of the locks. If all 3 challengeStates are true then it does the confetti thing and replaces the text on the challenge overlay with congrats.

# main.py changes
Just under the challenge state queries I do 3 new queries to get the splunk_challenges.key one/two/three, set 3 new variables for states, then do some if statements to determine if the splunk challenge is completed

```
# Get splunk challenges

splunkChall1  =  db.session.query(splunk_challenges.key_one).filter_by(user_id  =  current_user.id).first()
splunkChall2  =  db.session.query(splunk_challenges.key_two).filter_by(user_id  =  current_user.id).first()
splunkChall3  =  db.session.query(splunk_challenges.key_three).filter_by(user_id  =  current_user.id).first()


chall1State  =  False
chall2State  =  False
chall3State  =  False


# Check if challenge exists
if  splunkChall1:
	# If challenge is completed, set state to true
	if  splunkChall1[0] !=  0:
		chall1State  =  True
	# Else set state to false
	else:
		chall1State  =  False

# Same as above
if  splunkChall2:
	if  splunkChall2[0] !=  0:
		chall2State  =  True
	else:
		chall2State  =  False
  
if  splunkChall3:
	if  splunkChall3[0] !=  0:
		chall3State  =  True
	else:
		chall3State  =  False
```
Then these get passed into cyberescape using the render_template stuff
```
    if(laptopChallenge and phoneChallenge and serverChallenge):
        if(laptopChallenge[0] == 4 and phoneChallenge[0] == 3 and serverChallenge[0] == 4):
            keyValidator = Markup(constructKeyValidator)
            return render_template('cyberescape.html', user=current_user, userPoints = userPoints, userTime = timeLeft, keyValidator = keyValidator,chall1State = chall1State, chall2State = chall2State, chall3State = chall3State)
    
    return render_template('cyberescape.html', user = current_user, userPoints = userPoints, userTime = timeLeft, chall1State = chall1State, chall2State = chall2State, chall3State = chall3State)
```
# cyberescape.html changes
I believe you can just copy paste the code from here
https://github.com/40484357/CaptureTheFlag/blob/win-room-rework/webapp/templates/cyberescape.html
It uses js at the bottom to read in the challStates and change lock pics accordingly, also does the confetti stuff in that script.

# script.js changes
two new functions to deal with opening and closing the overlay
```
function showHelpModal(){
    if(document.getElementById('helpOverlayModal').style.display == "none"){
        document.getElementById('helpOverlayModal').style.display = "block";
    }
}
function closeHelpModal(){
    if(document.getElementById('helpOverlayModal').style.display != "none"){
        document.getElementById('helpOverlayModal').style.display = "none";
    }
}
```
# styles.css changes
just some new css for the new things
```
    .closeHelpModal{
        position: absolute;
        top: 15px;
        right: 35px;
        color: #f1f1f1;
        font-size: 40px;
        font-weight: bold;
        transition: 0.3s;
    }

    .closeHelpModal:hover,
    .closeHelpModal:focus {
    color: #bbb;
    text-decoration: none;
    cursor: pointer;
    }
    .helpOverlayModalButton{
        float: left;
        color: white;
        width:60px;
        height: 60px;
        font-size: 50px;
        border: white solid 2px;
        text-align: center;
        border-radius:50%;
    }
    .helpOverlayModalButton:hover{
        background-color: white;
        color: #0B0909;
        cursor: pointer;
    }

    #helpOverlayModal{
        padding:10px;
        border: white solid 2px;
        border-radius: 10px;
        position: fixed;
        z-index: 1;
        left: 30%;
        top: 40%;
        width: 40%;
        height: 30%;
        overflow: auto;
        /* Fallback color */
        background-color: #0E294B;

    }
    #helpOverlayModal h1{
        color: rgb(255, 255, 255);
        font-size: 30px;
        text-align: center;
    }
    #helpOverlayModal p{
        color: rgb(255, 255, 255);
        font-size: 20px;
    }
    #helpOverlayModal #copyScript{
        color: black;
        font-size: 20px;
        margin-left: 50px;
        margin-top: 10px;
        margin-bottom: 10px;
        border: black solid 2px;
        border-radius: 10px;
        padding: 5px;
        cursor: pointer;

    }

    #laptopLock{
        position: relative;
        background:url(./locked.png);
        background-size: contain;
        height:7vb;
        width: 5vb;
        left: 32%;
        bottom: 35%;
        position: relative;
    }
    #phoneLock{
        position: relative;
        background:url(./locked.png);
        background-size: contain;
        height:7vb;
        width: 5vb;
        left: 58%;
        bottom: 25%;
        position: relative;
    }
    #serverLock{
        position: relative;
        background:url(./locked.png);
        background-size: contain;
        height:7vb;
        width: 5vb;
        left: 69%;
        bottom: 20%;
        position: relative;
    }
   ```
   # the two lock pictures
   can be downloaded here
   https://github.com/40484357/CaptureTheFlag/blob/win-room-rework/webapp/static/unlocked.png
   and 
   
   here
   https://github.com/40484357/CaptureTheFlag/blob/win-room-rework/webapp/static/locked.png
   
Think that's everything, if it looks wrong let me know and i'll have a look

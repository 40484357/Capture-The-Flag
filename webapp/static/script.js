var continueButton = document.getElementById('continue')
var back = document.getElementById('back')
var quizButton = document.getElementById('quizButton')
var firstScene = document.getElementById('firstScene')
var secondScene = document.getElementById('secondScene')

/* states
0 = story intro
1 = asking user to take quiz
2 = asking user if they are ready to begin
3 = quiz
*/

var state = 0
//Quiz variables
var quiz = [];
quiz[0] = new Question("Which country has the most number of cameras?\n Check 'camera' in https://www.shodan.io/", "United States", "United Kingdom", "China","Germany");
quiz[1] = new Question("Has napierstudent2023@gmail.com been pwned (https://haveibeenpwned.com/)", "No", "Yes", "Yes, 3 data breaches","Yes, 1 data breach");
quiz[2] = new Question("What is the ip address of ns3 server of napier university (napier.ac.uk)?\n Use link https://www.whois.com/whois", "146.176.7.1", "146.196.7.1", "146.186.7.1","146.176.10.1");
quiz[3] = new Question("Sock puppets are online fictitious identities of the OSINT investigator, to gain access to information that requires an account to access such as social media sites. Which resources can be used to create this fictitious identity?", "All of these", "This person does not exist", "Fake name generator","Privacy cards");
quiz[4] = new Question("Which of the following is the best OSINT application to verify whether company data is available publicly?", "theHarvester", "Cuckoo", "Nmap","Nessus");
quiz[5] = new Question("An application log containing the following, is an indication of what type of breach? https://www.comptia.com/login.php?id='%20or%20'1'1='1", "SQLi", "DLL Injection", "API attack","XSS");
quiz[6] = new Question("Which of the following would be indicative of a hidden audio file found inside of a piece of source code?", "Steganography", "Homomorphic encryption", "Cipher suite","Blockchain");
quiz[7] = new Question("What is the open-source framework used by cyber security professionals to conduct footprinting and reconnaissance activities?","OSINT framework","WebSploit Framework","Browser Exploitation Framework","SpeedPhish Framework");
quiz[8] = new Question("Which country has the most number of printers? Check 'printer' in https://www.shodan.io/","China","South Korea","United States","France");
quiz[9] = new Question("Searchcode is to check for sensitive information present within the source code of computer programs (searchcode.com). What is the first email address you come across with password1234! as the password?","rvasquez@gmail.com","joeblog@yahoo.com","rvasquez@jclouds.org","patkennedy79@yahoo.com")
var randomQuestion;
var answers = [];
var currentScore = 0;

function Question(question,rightAnswer,wrongAnswer1,wrongAnswer2, wrongAnswer3) { // Question constructor
    this.question = question;
    this.rightAnswer = rightAnswer;
    this.wrongAnswer1 = wrongAnswer1;
    this.wrongAnswer2 = wrongAnswer2;
    this.wrongAnswer3 = wrongAnswer3;
};

function shuffle(o) { // Shuffles the answers after they are put in the array
	for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
};

function genQuestion() { // Generates a random question and displays it
  
    if(quiz.length > 5) { // Only give the user 5 questions from the list
        var randomNumber = Math.floor(Math.random()*quiz.length);
        randomQuestion = quiz[randomNumber]; //getQuestion
        quiz.splice(randomNumber,1); //removeQuestionFromQuiz
        answers = [randomQuestion.rightAnswer, randomQuestion.wrongAnswer1, randomQuestion.wrongAnswer2, randomQuestion.wrongAnswer3];
        shuffle(answers);
    
        document.getElementById("question").innerHTML= randomQuestion.question;
        document.getElementById("answerA").value= answers[0];
        document.getElementById("answerA").innerHTML= answers[0];
        document.getElementById("answerB").value= answers[1];
        document.getElementById("answerB").innerHTML= answers[1];
        document.getElementById("answerC").value= answers[2];
        document.getElementById("answerC").innerHTML= answers[2];
        document.getElementById("answerD").value= answers[3];
        document.getElementById("answerD").innerHTML= answers[3];
    }
    else{
       document.getElementById("question").innerHTML= "You have finished the quiz! Your score is: " + currentScore+"/5";
       document.getElementById("answerA").classList.add('hidden');
       document.getElementById("answerB").classList.add('hidden');
       document.getElementById("answerC").classList.add('hidden');
       document.getElementById("answerD").classList.add('hidden');
       document.getElementById("retry").classList.remove('hidden');
    }
}

function answerA_clicked() {
  var answerA = document.getElementById("answerA").value;
  checkAnswer(answerA);
}

function answerB_clicked() {
  var answerB = document.getElementById("answerB").value;
  checkAnswer(answerB);
}
function answerC_clicked() {
  var answerC = document.getElementById("answerC").value;
  checkAnswer(answerC);
}

function answerD_clicked() {
    var answerD = document.getElementById("answerD").value;
    checkAnswer(answerD);
}
function adjustScore(isCorrect) {
  if (isCorrect) {
    currentScore++;
  } else {
    if (currentScore > 0) {
      currentScore--;
    }
  }
  document.getElementById("score").innerHTML = currentScore;
}

function checkAnswer(answer) {
  if (answer == randomQuestion.rightAnswer) {
    adjustScore(true);
    genQuestion();
  } else {
    adjustScore(false);
  }
}
  
  

if(continueButton != null){
continueButton.addEventListener('click', ()=>{
    if(state==0){
        var descript = document.getElementById('descriptText')
        var quizButton = document.getElementById('quizButton')
        var backButton = document.getElementById('back')

        descript.innerHTML="We need to make sure you're the right person for the job. Test your eligibility by taking this short quiz."
        quizButton.classList.remove('hidden')
        backButton.classList.remove('hidden')

        state = 1
        return
    }
    if(state==1){
        var quizButton = document.getElementById('quizButton')
        quizButton.classList.add('hidden')
        var descript = document.getElementById('descriptText')
        descript.innerHTML="Now, are you ready to begin? If so, click continue to begin the challenge."
        state = 2
        return
    }
    if(state==3){
        var quiz = document.getElementById('introQuiz')
        var backButton = document.getElementById('back')
        var quizbtn = document.getElementById('quizButton')
        var descript = document.getElementById('descriptText')
        descript.innerHTML="Now, are you ready to begin? If so, click continue to begin the challenge."
        quiz.classList.add('hidden')
        //quizbtn.classList.remove('hidden')
        backButton.classList.remove('hidden')
        descript.classList.remove('hidden')
        state = 2
        return
    }
    if(state==2){
        startTimer();
        window.location.href='/cyberescape'
    }

    
})}

if(back != null){
back.addEventListener('click', ()=>{
    if(state==1)
    {
        var descript = document.getElementById('descriptText')
        var quizButton = document.getElementById('quizButton')
        var backButton = document.getElementById('back')

        descript.innerHTML="<p>Laundromats Inc. are involved in money laundering. You have been given three pieces of evidence</p><ol><li>a laptop</li><li>a mobile phone</li><li>a server</li></ol><p>You have 24 hours to forensically analyse the evidence by solving the challenges.</p>"
        quizButton.classList.add('hidden')
        backButton.classList.add('hidden')

        state = 0
        return
    }
    if(state==2)
    {
        var descript = document.getElementById('descriptText')
        var quizButton = document.getElementById('quizButton')
        var backButton = document.getElementById('back')

        descript.innerHTML="We need to make sure you're the right person for the job. Test your eligibility by taking this short quiz."
        quizButton.classList.remove('hidden')
        backButton.classList.remove('hidden')

        state = 1
        return
    }
    if(state==3)
    {
        var descript = document.getElementById('descriptText')
        var quiz = document.getElementById('introQuiz')
        var backButton = document.getElementById('back')
        var quizbtn = document.getElementById('quizButton')

        descript.innerHTML="We need to make sure you're the right person for the job. Test your eligibility by taking this short quiz."
        quiz.classList.add('hidden')
        quizbtn.classList.remove('hidden')
        backButton.classList.remove('hidden')
        descript.classList.remove('hidden')

        state = 1
        return
    }

})}

if(quizButton != null){
quizButton.addEventListener('click', ()=>{
    state = 3
    genQuestion();
    var descript = document.getElementById('descriptText')
    var quizbtn = document.getElementById('quizButton')
    var quiz = document.getElementById('introQuiz')
    descript.classList.add('hidden')
    quizbtn.classList.add('hidden')
    quiz.classList.remove('hidden')

})}


function hideScene(Element){
    Element.classList.add('hidden')
    Element.classList.remove('gameLauncher')
} //fast hider of scenes

function showScene(Element){
    Element.classList.remove('hidden')
    Element.classList.add('gameLauncher')
} //fast shower of scenes

function goToLaptop(){
    window.location.href = '/laptop'
} //goes to laptop

function goToPhone(){
    window.location.href = '/phone'
} //goes to phone

function goToWinroom(){
    window.location.href = '/winroom'
} //goes to winroom

function goToServer(){
    window.location.href = '/server'
}

function copyTextToClipboard(hash){
	navigator.clipboard.writeText(hash.textContent);
  alert('Copied text to clipboard!');
} // Copies hash to clipboard

function goToEvidence(){
    window.location.href = '/cyberescape'
} //goes to evidence

function goToWeb(){
    window.location.href = '/'
} //goes to web

let Time_Limit = 86400;
function getTimeLimit(timeLimit){
    Time_Limit = timeLimit
    localStorage.setItem('timeLeft', Time_Limit)
}
let timePassed = 0;
let timeLeft = Time_Limit;
const FULL_DASH_ARRAY = 283;
const Warning_threshold = 3600;
const Alert_threshold = 1800;

const COLOUR_CODES = {
    info: {
        colour: "green"
    },
    warning: {
        colour: "orange",
        threshold: Warning_threshold
    },
    alert: {
        colour: "red",
        threshold: Alert_threshold
    }
}

let remainingPathColor = COLOUR_CODES.info.colour;


let timerInterval = null;

document.getElementById('clock').innerHTML = 
`
    <div class="clockBase">
        <svg class="clockBase_svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <g class="clockBase_circle">
        <circle class="clockBase_path-elapsed" cx="50" cy="50" r="45" />
        <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
        ></path>
        </g>
        </svg>
        <span id="clockBase_timer_label" class="clockBase_label">
            ${timerCountdown(timeLeft)}
        </span>
    </div>
`;

function timerCountdown(time){
    const hours = Math.floor((time/60)/60)
    let minutes = Math.floor((time/60)%60);
    let seconds = time%60;
    if(seconds<10){
        seconds = `0${seconds}`;
    }
    if(minutes<10){
        minutes = `0${minutes}`
    }

    return `${hours}:${minutes}:${seconds}`;
}


function getHint(challenge){
    let currentHint = ""
    var hintBox = document.getElementById('hintDiv')
    var hintText = document.getElementById('hintText')
    
    const url = 'http://127.0.0.1:5000/hints'

    fetch(url)
    .then(response => response.json())
    .then((jsonData) =>{
        for(const[key, value] of Object.entries(jsonData)){
            if(value.name === challenge){
                currentHint = value.hint
                hintText.innerHTML = currentHint
            }
        }

    })

    

    const request = new XMLHttpRequest()
    request.open('POST', `updateHints/${challenge}`)
    request.send()
   
    hintBox.classList.remove('hidden')

    
}

function goToSplunk(){
    window.location.href = '/splunk'
}

function closeHint(){
    var hintBox = document.getElementById('hintDiv')
    hintBox.classList.add('hidden')
}


function startTimer(){
    if(localStorage.getItem('timeLeft') == null){
        localStorage.setItem('timeLeft', timeLeft)
    } else {
        Time_Limit = localStorage.getItem('timeLeft')
    }
    timerInterval = setInterval(()=>{
        timePassed = timePassed += 1;
        timeLeft = Time_Limit - timePassed;
        localStorage.setItem('timeLeft', timeLeft)
        document.getElementById('clockBase_timer_label').innerHTML = timerCountdown(timeLeft);
        setCircleDasharray();
        setRemainingPathColour(timeLeft);
        if(timeLeft == 0){
            onTimesUp();
        }

    }, 1000)
}

startTimer();

function setRemainingPathColour(timeLeft){
    const {alert, warning, info} = COLOUR_CODES;
    const pathColour = document.getElementById('base-timer-path-remaining')
    if(timeLeft <= alert.threshold){
        pathColour.classList.remove(warning.colour)
        pathColour.classList.add(alert.colour)
    } else if(timeLeft <= warning.threshold){
        pathColour.classList.remove(info.colour)
        pathColour.classList.add(warning.colour)
    }
}

function calculateTimeFraction() {
    const rawTimeFraction = timeLeft / Time_Limit;
    return rawTimeFraction - (1 / Time_Limit) * (1 - rawTimeFraction);
}

function setCircleDasharray() {
    const circleDasharray = `${(
      calculateTimeFraction() * FULL_DASH_ARRAY
    ).toFixed(0)} 283`;
    document
      .getElementById("base-timer-path-remaining")
      .setAttribute("stroke-dasharray", circleDasharray);
}
function openNotesApp(){
    document.getElementById('notesButton').style.display='none';
    document.getElementById('aesFileButton').style.display='none';
    document.getElementById('photosButton').style.display='none';
    document.getElementById('decodeButton').style.display='none';
    document.getElementById('phoneHome').style.background='none';
    document.getElementById('phoneHome').style.backgroundColor='#f3f198';
    document.getElementById('backButtonNotes').style.display='flex';
    document.getElementById('notesApp').style.display='flex';
    document.getElementById('aesMessage').style.display='none';
    document.getElementById('aesFlash').style.display='none';
}

function closeNotesApp(){
    var backgroundImageUrl = "url('../static/phoneBackground.jpeg')"
    document.getElementById('notesButton').style.display='block';
    document.getElementById('aesFileButton').style.display='block';
    document.getElementById('photosButton').style.display='block';
    document.getElementById('decodeButton').style.display='block';
    document.getElementById('phoneHome').style.backgroundImage= backgroundImageUrl;
    document.getElementById('phoneHome').style.backgroundSize='cover';
    document.getElementById('phoneHome').style.backgroundColor='none';
    document.getElementById('backButtonNotes').style.display='none';
    document.getElementById('notesApp').style.display='none';
}

function openAesApp()
{
    document.getElementById('notesButton').style.display='none';
    document.getElementById('aesFileButton').style.display='none';
    document.getElementById('photosButton').style.display='none';
    document.getElementById('decodeButton').style.display='none';
    document.getElementById('phoneHome').style.background='none';
    document.getElementById('phoneHome').style.backgroundColor='grey';
    document.getElementById('backButtonAes').style.display='flex';
    document.getElementById('aesApp').style.display='flex';
    document.getElementById('aesLock').style.display='block';
    document.getElementById('aesMessage').style.display='none';
    document.getElementById('aesFlash').style.display='none';
   
}
function closeAesApp()
{
    var backgroundImageUrl = "url('../static/phoneBackground.jpeg')"
    document.getElementById('notesButton').style.display='block';
    document.getElementById('aesFileButton').style.display='block';
    document.getElementById('photosButton').style.display='block';
    document.getElementById('decodeButton').style.display='block';
    document.getElementById('phoneHome').style.backgroundImage= backgroundImageUrl;
    document.getElementById('phoneHome').style.backgroundSize='cover';
    document.getElementById('phoneHome').style.backgroundColor='none';
    document.getElementById('backButtonAes').style.display='none';
    document.getElementById('aesApp').style.display='none';
    document.getElementById('aesLock').style.display='none';
    
}
// Stuff for steganography
// Get the modal
var modal = document.getElementById("steganoModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("photosButton");
var modalImg = document.getElementById("forensicimage.png");
var captionText = document.getElementById("caption");
if(img){
img.onclick = function(){
  modal.style.display = "block";
  captionText.innerHTML = "Looks like a normal image... or is it?";
}}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
if(span){
span.onclick = function() {
  modal.style.display = "none";
}}


//script for base64 

var file = document.getElementById('file1')
var openBase64 = document.getElementById('openBase64')
var txt_file_tab = document.getElementById('txt_file_tab')
var ipCheck = document.getElementById('ipcheck')
var openIP = document.getElementById('openIP')
var minimizeIP = document.getElementById('minimize_IP')
var closeIP = document.getElementById('close_IP')
var ipTab = document.getElementById('ip_tab')

if(file){
file.addEventListener('click', () => {
   
    openBase64.classList.remove('hidden')
    txt_file_tab.classList.remove('hidden')
    ipCheck.classList.add('hidden')
})}

var close_file = document.getElementById('close_file')

if(close_file){
close_file.addEventListener('click', ()=>{
    openBase64.classList.add('hidden')
    txt_file_tab.classList.add('hidden')    
})}

if(txt_file_tab){
txt_file_tab.addEventListener('click', ()=>{
    if (openBase64.classList.contains('hidden')){
        openBase64.classList.remove('hidden')
        ipCheck.classList.add('hidden')
    } else {
        openBase64.classList.add('hidden')
    }
})}

var minimize_file = document.getElementById('minimize_file')
if(minimize_file){
minimize_file.addEventListener('click', () =>{
    openBase64.classList.add('hidden')
})}

if(openIP){
openIP.addEventListener('click', ()=>{
    ipCheck.classList.remove('hidden')
    openBase64.classList.add('hidden')
    ipTab.classList.remove('hidden')
    localStorage.setItem('openIP', 'true')
})}

if(minimizeIP){
minimizeIP.addEventListener('click', ()=>{
    ipCheck.classList.add('hidden')
    localStorage.setItem('openIP', 'false')
})}

if(closeIP){
closeIP.addEventListener('click', () => {
    ipCheck.classList.add('hidden')
    ipTab.classList.add('hidden')
    localStorage.setItem('openIP', 'false')
})}

if(ipTab){
ipTab.addEventListener('click', () => {
    if(ipCheck.classList.contains('hidden')){
        ipCheck.classList.remove('hidden')
        openBase64.classList.add('hidden')
        localStorage.setItem('openIP', 'false')
    } else {
        ipCheck.classList.add('hidden')
        localStorage.setItem('openIP', 'true')
    }
})}

function checkOpenIp(){
    if(localStorage.getItem('openIP') == 'true'){
        if(ipCheck){
        ipCheck.classList.remove('hidden')
        }
    }
}

checkOpenIp()
var toast = document.getElementById('toast')


function fade(element){
    var op = 1; 
    var timer = setInterval(function (){
        if(op<=0.1){
            clearInterval(timer)
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity='+ op * 100 + ')';
        op -= op * 0.1;
    }, 110);
}

if(toast){
fade(toast)
}


function dial(number){
    //add number to passcode form
    var passcode = document.getElementById('phoneAnswer')
    passcode.value += number
    console.log(number)
}
function backspace(){
    //remove last number from passcode form
    var passcode = document.getElementById('phoneAnswer')
    passcode.value = passcode.value.slice(0, -1)
}
function selectAccountType(){
    var student = document.getElementById('student')
    var lecturer = document.getElementById('lecturer')
    var studentForm = document.getElementById('student-form')
    var lecturerForm = document.getElementById('lecturer-form')

    if(lecturer.checked == true){
        studentForm.classList.add("hidden");
        lecturerForm.classList.remove("hidden");
    }
    else if(student.checked == true){
        lecturerForm.classList.add("hidden");
        studentForm.classList.remove("hidden");
    }

}
function openProfile() {
    document.getElementById("side-profile-background").style.left = "0";
    document.getElementById("side-profile-background").style.opacity = "1";
    document.getElementById("side-profile").style.right = "0";


  
}
function closeProfile(){
    document.getElementById("side-profile-background").style.opacity = "0";
    setTimeout(slideLeft, 500);
    document.getElementById("side-profile").style.right = "-30%";
}
function slideLeft(){
    document.getElementById("side-profile-background").style.left = "100%";
}
function codeDisplay(){
    document.getElementById("code-popup-bg").style.left = "0";
    document.getElementById("code-popup-bg").style.opacity = "1";
    document.getElementById("code-popup").style.left = "35%";
    document.getElementById("code-popup").style.top = "30%";
}
function codeHide(){
    document.getElementById("code-popup-bg").style.opacity = "0";
    setTimeout(hidePopup, 500);
    document.getElementById("code-popup").style.right = "0";
    document.getElementById("code-popup").style.bottom = "0";

   
    
   
}
function hidePopup(){
   
    document.getElementById("code-popup-bg").style.left = "100%";
}

function disappear(){
    setTimeout(none, 2000)
    setTimeout(none2,3000)
   }
   function none(){
       document.getElementById('account-success').style.opacity = '0';
   }
   function none2(){
    document.getElementById('account-success').style.left = '100%';
}

function showHelp(){
    if(document.getElementById('helpOverlay').classList.contains('hidden')){
        document.getElementById('helpOverlay').classList.remove('hidden');
    }
    else{
        document.getElementById('helpOverlay').classList.add('hidden');
    }
}
function copyScript(){
    navigator.clipboard.writeText("PGltZyBzcmM9eCBvbmVlcnJvcj1hbGVydChkb2N1bWVudC5jb29raWUpPg==");
    alert('Copied data to clipboard!');
}
function scriptPanel(){
    if(document.getElementById('browserBottom').classList.contains('hidden')){
        document.getElementById('browserBottom').classList.remove('hidden');
    }
    else{
        document.getElementById('browserBottom').classList.add('hidden');
    }
}
function closeAlert(){
    document.getElementById('popupAlert').classList.add('hidden');
}
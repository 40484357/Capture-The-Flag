
Hey, here's the intro code in chunks to replace over the current system. If you find it easier, the github commit log is here: https://github.com/40484357/CaptureTheFlag/commit/dbdf24cfcf97e5899bffcfa7f43157969f588e87
But I'll type out the changes like i did for the web challenge.

For intro.html, I think you can just copy paste the entire thing over the current one.

In script.js, just under line 14, var state = 0, you can copy paste this in for the logic:

```//Quiz variables
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
```

Next, near line 108, the commented out link to kahoot can be replaced by: `genQuestion();`


For styles.css, I'll give the changes first, then the new chunks. 

Changes:

near line 654, .descriptText{
`background: rgba(18, 15, 14, 0.9);` instead of `background: rgba(204, 101, 57, 0.38);`
`padding:2em`; instead of `padding:1em;`


near line 737, #introQuiz can be replaced with
```
#introQuiz {
    width: 1000px;
    margin: auto;
    text-align: center;
    border-radius: 14px
}
```


New blocks:

```
.descriptText button {
    height: 40px;
    width: 200px;
    outline: none;
    background: white;
    border: black solid 2px;
}
#score, #scoreText{ /*styling of the score box*/
    float:inline-start;
    margin: 0.1em;
    font-size: 30px;
    font-family: 'public sans';
    color: #ffffff;
}

.answerBoxes{ /*spacing of the answer boxes*/
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
    height: 100%;
    margin: auto;
    padding: 1em;
    gap: 1em;
}
#answerA,#answerB,#answerC,#answerD{ /*styling of the answer boxes*/
    background: rgba(204, 101, 57, 1);
    border-radius: 14px;
    padding: 1em;
    font-family: 'public sans';
    font-style: normal;
    font-weight: 400;
    font-size: 17px;
    line-height: 193.9%;
    color: #FFFFFF;
    width: 100%;
    height: 100%;
    text-align: center;
}
#retry{
    background: rgba(204, 101, 57, 1);
    border-radius: 14px;
    padding: 1em;
    font-family: 'public sans';
    font-style: normal;
    font-weight: 400;
    font-size: 17px;
    line-height: 193.9%;
    color: #FFFFFF;
    width: 40%;
    height: 100%;
    text-align: center;
}
#answerA:hover,#answerB:hover,#answerC:hover,#answerD:hover,#retry:hover{ /*hover styling of the answer boxes*/
    background: rgba(204, 101, 57, 0.65);
    cursor: pointer;
}
```

Think thats it all, hope it makes sense, let me know if it doesn't and we can set up a call next week to fix it



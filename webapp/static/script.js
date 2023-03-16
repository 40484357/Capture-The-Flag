var continueButton = document.getElementById('continue')
var firstScene = document.getElementById('firstScene')
var secondScene = document.getElementById('secondScene')

if(continueButton != null){
continueButton.addEventListener('click', ()=>{
    hideScene(firstScene)
    showScene(secondScene)
    startTimer();
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


function copyTextToClipboard(hash){
	navigator.clipboard.writeText(hash.textContent);
  alert('Copied text to clipboard!');
} // Copies hash to clipboard

let Time_Limit = 86400;
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
};

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

function checkTimer(){
    if(localStorage.getItem('timerStatus') == 'true'){
        startTimer();
    }
}

checkTimer();


function startTimer(){
    if(localStorage.getItem('timeLeft') == null){
        localStorage.setItem('timeLeft', timeLeft)
    } else {
        Time_Limit = localStorage.getItem('timeLeft')
    }

    if(localStorage.getItem('timerStatus') == null){
        localStorage.setItem('timerStatus', true)
    }
    
    timerInterval = setInterval(()=>{
        timePassed = timePassed += 1;
        timeLeft = Time_Limit - timePassed;
        document.getElementById('clockBase_timer_label').innerHTML = timerCountdown(timeLeft);
        setCircleDasharray();
        setRemainingPathColour(timeLeft);
        localStorage.setItem('timeLeft', timeLeft)
        if(timeLeft == 0){
            onTimesUp();
        }

    }, 1000)
}

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
img.onclick = function(){
  modal.style.display = "block";
  captionText.innerHTML = "Looks like a normal image... or is it?";
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}


//script for base64 

var file = document.getElementById('file1')
var openBase64 = document.getElementById('openBase64')
var txt_file_tab = document.getElementById('txt_file_tab')
var ipCheck = document.getElementById('ipcheck')
var openIP = document.getElementById('openIP')
var minimizeIP = document.getElementById('minimize_IP')
var closeIP = document.getElementById('close_IP')
var ipTab = document.getElementById('ip_tab')

file.addEventListener('click', () => {
   
    openBase64.classList.remove('hidden')
    txt_file_tab.classList.remove('hidden')
    ipCheck.classList.add('hidden')
})

var close_file = document.getElementById('close_file')


close_file.addEventListener('click', ()=>{
    openBase64.classList.add('hidden')
    txt_file_tab.classList.add('hidden')    
})

txt_file_tab.addEventListener('click', ()=>{
    if (openBase64.classList.contains('hidden')){
        openBase64.classList.remove('hidden')
        ipCheck.classList.add('hidden')
    } else {
        openBase64.classList.add('hidden')
    }
})

var minimize_file = document.getElementById('minimize_file')
minimize_file.addEventListener('click', () =>{
    openBase64.classList.add('hidden')
})



openIP.addEventListener('click', ()=>{
    ipCheck.classList.remove('hidden')
    openBase64.classList.add('hidden')
    ipTab.classList.remove('hidden')
    localStorage.setItem('openIP', 'true')
})

minimizeIP.addEventListener('click', ()=>{
    ipCheck.classList.add('hidden')
    localStorage.setItem('openIP', 'false')
})

closeIP.addEventListener('click', () => {
    ipCheck.classList.add('hidden')
    ipTab.classList.add('hidden')
    localStorage.setItem('openIP', 'false')
})

ipTab.addEventListener('click', () => {
    if(ipCheck.classList.contains('hidden')){
        ipCheck.classList.remove('hidden')
        openBase64.classList.add('hidden')
        localStorage.setItem('openIP', 'false')
    } else {
        ipCheck.classList.add('hidden')
        localStorage.setItem('openIP', 'true')
    }
})

function checkOpenIp(){
    if(localStorage.getItem('openIP') == 'true'){
        ipCheck.classList.remove('hidden')
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
    }, 75);
}

fade(toast)
function dial(number){
    //add number to passcode form
    var passcode = document.getElementById('phoneAnswer')
    passcode.value += number
}
function backspace(){
    //remove last number from passcode form
    var passcode = document.getElementById('phoneAnswer')
    passcode.value = passcode.value.slice(0, -1)
}


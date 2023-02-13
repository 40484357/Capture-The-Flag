var continueButton = document.getElementById('continue')
var firstScene = document.getElementById('firstScene')
var secondScene = document.getElementById('secondScene')

continueButton.addEventListener('click', ()=>{
    hideScene(firstScene)
    showScene(secondScene)
})

function hideScene(Element){
    Element.classList.add('hidden')
    Element.classList.remove('gameLauncher')
} //fast hider of scenes

function showScene(Element){
    Element.classList.remove('hidden')
    Element.classList.add('gameLauncher')
} //fast shower of scenes


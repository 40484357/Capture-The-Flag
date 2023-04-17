let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    cartItem.classList.remove('active');
}

let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    cartItem.classList.remove('active');
}


window.onscroll = () =>{
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
    cartItem.classList.remove('active');
}



/*=============== LOADING ICON ===============*/
onload = () => {
    const load = document.getElementById('loader')

    setTimeout(() => {
        load.style.display = 'none'
    }, 2500)
}



/*=============== SHOW SCROLLING ===============*/
function scrollIcon() {
    const scrollIcon = document.getElementById('scroll-Icon');
    // When the scroll is higher than 350 viewport height, add the show-scroll class to the a tag with the scroll-top class
    if (this.scrollY >= 350) scrollIcon.classList.add('show-scroll'); else scrollIcon.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollIcon)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 58,
            sectionId = current.getAttribute('id')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
        } else {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/*
var dc = document.cookie;
13:20:26.700 undefined
13:21:05.442 if(dc = 'username = admin'){
    window.location = ('127.0.0.1:5000/laptop')
}
13:21:05.467 '127.0.0.1:5000/laptop'
13:21:14.102 if(dc = 'username = admin'){
    window.location = ('/laptop')
}
13:21:14.113 '/laptop'
*/
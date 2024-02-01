// navbar responsive
var barx = document.querySelector('#bar')
var navbar = document.querySelector('#navbar')
var closeIcon = document.querySelector('#close')
closeIcon.style.red = "red"

if (barx) {
    barx.addEventListener('click', () => {
        navbar.classList.add('active');
        closeIcon.style.display = "initial"
        console.log("working")
    })
}
if (closeIcon) {
    closeIcon.addEventListener('click', () => {
        navbar.classList.remove('active');
        closeIcon.style.display = "none"
        console.log("working2")
    })
}

// Sprouduct details scripts
var mainImg = document.getElementById("mainImg")
var small = document.getElementsByClassName("smallImg")

small[0].onclick = function() {
    mainImg.src = small[0].src; 
}

small[1].onclick = function() {
    mainImg.src = small[1].src; 
}

small[2].onclick = function() {
    mainImg.src = small[2].src; 
}

small[3].onclick = function() {
    mainImg.src = small[3].src; 
}

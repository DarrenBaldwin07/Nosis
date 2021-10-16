
const hamburger = document.querySelector('.menu');
const menu = document.querySelector('.links');


console.log(menu.style.display);


hamburger.addEventListener('click', () => {

    menu.classList.add('mobile-menu');
    

    if (menu.style.display === "none") {
        menu.style.display = 'flex';
    } else if(menu.style.display === 'flex') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'flex';
    }
});
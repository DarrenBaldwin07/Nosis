




const percent = document.querySelectorAll('.percent');
const progressbar = document.querySelectorAll('.red');

let counter = 0;

percent.forEach(i => {
    
    progressbar[counter].style.width = String((i.innerHTML.replace('%', '') * 1)).concat('%');
    counter++
    
});

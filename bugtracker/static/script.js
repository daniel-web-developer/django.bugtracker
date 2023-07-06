const menu = document.querySelector('#menu');
const overlay = document.querySelector('#overlay');

menu.addEventListener('click', () => {
    console.log("VIVA CRISTO REY");
    if(menu.classList.contains('open')){
        menu.classList.remove('open');
    }
    else{
        menu.classList.add('open');
    }

    if(overlay.classList.contains('overlay-active')){
        overlay.classList.remove('overlay-active');
    }
    else{
        overlay.classList.add('overlay-active');
    }
})
const menu = document.querySelector('#menu');
const overlay = document.querySelector('#overlay');
const button = document.querySelector('#delete-button');
const confirm = document.querySelector('#confirmation');
const yea = document.querySelector('#conf-yes');
const nay = document.querySelector('#conf-no');

menu.addEventListener('click', () => {
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
});

button.addEventListener('click', () => {
    confirm.classList.toggle('ticket-confirm-dn');
})

nay.addEventListener('click', () => {
    confirm.classList.toggle('ticket-confirm-dn');
})


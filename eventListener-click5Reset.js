const container = document.querySelector('#container');
const pText = document.querySelector('p');
const button = document.querySelector('#button1');
let text = '';
let count = 0;

function writeText() {
    count += 1;
    text += 'rock1<br>';
    pText.innerHTML = text;
    if (count >= 5) {
        container.removeChild(button);
        const buttonReset = document.createElement('button');
        buttonReset.setAttribute('id', 'button2');
        buttonReset.innerText = "Reset!";
        container.appendChild(buttonReset);
        buttonReset.addEventListener('click', () => {
            pText.innerText = '';
            text = '';
            count = 0;
            container.removeChild(buttonReset);
            container.prepend(button);
        })
    }
}

button.addEventListener('click', writeText)

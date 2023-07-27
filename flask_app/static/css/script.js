// ||Dark mode/ Light mode button||


const body = document.querySelector('body');
const btn = document.querySelector('.btn');
const icon = document.querySelector('.btn__icon');

//to save the dark mode use the object "local storage".

//function that stores the value true if the dark mode is activated or false if it's not.
function store(value) {
    localStorage.setItem('darkmode', value);
}

//function that indicates if the "darkmode" property exists. It loads the page as we had left it.
function load() {
    const darkmode = localStorage.getItem('darkmode');

    //if the dark mode was never activated
    if (!darkmode) {
        store(false);
        icon.classList.add('fa-sun');
    } else if (darkmode == 'true') { //if the dark mode is activated
        body.classList.add('darkmode');
        icon.classList.add('fa-moon');
    } else if (darkmode == 'false') { //if the dark mode exists but is disabled
        icon.classList.add('fa-sun');
    }
}


load();

btn.addEventListener('click', () => {

    body.classList.toggle('darkmode');
    icon.classList.add('animated');

    //save true or false
    store(body.classList.contains('darkmode'));

    if (body.classList.contains('darkmode')) {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    } else {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }

    setTimeout(() => {
        icon.classList.remove('animated');
    }, 500)
})



// Search
const chatlog = document.getElementById('chatlog');
        const userInput = document.getElementById('user_input');
        const sendButton = document.getElementById('send_button');

        function appendMessage(userMessage, chatbotMessage) {
            const messageDiv = document.createElement('div');
            messageDiv.innerHTML = `<strong>You:</strong> ${userMessage}<br><strong>ChatGPT:</strong> ${chatbotMessage}<hr>`;
            chatlog.appendChild(messageDiv);
        }
        function sendMessage() {
            const userMessage = userInput.value;
            appendMessage(userMessage, 'Loading...');
            userInput.value = '';
            fetch('/ask', {
                method: 'POST',
                body: new URLSearchParams({ user_message: userMessage }),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then( response => response.json())
            .then(data => {
                const chatbotMessage = data.response;
                appendMessage(userMessage, chatbotMessage);
            })
            .catch(error => console.error('Error:', error));
        }
        userInput.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        });
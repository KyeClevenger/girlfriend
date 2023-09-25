// ||Dark mode/ Light mode button||
const body = document.querySelector('body');
const btn = document.querySelector('.btn');
const icon = document.querySelector('.btn__icon');
const chatlog = document.getElementById('chatlog');
const userInput = document.getElementById('user_input');
const sendButton = document.getElementById('send_button');
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

function appendMessage(userMessage, chatbotMessage) {
    const messageDiv = document.createElement('div');
    messageDiv.innerHTML = `<strong>You:</strong> ${userMessage}<br><strong>Partner:</strong> ${chatbotMessage}`;
    chatlog.appendChild(messageDiv);
}

function sendMessage() {
    const userMessage = userInput.value;
    userInput.value = '';

    fetch('/ask', {
        method: 'POST',
        body: new URLSearchParams({ user_message: userMessage }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
        .then(response => response.json())
        .then(data => {
            const chatbotMessage = data.response;
            // const elevenlabsMessage = data.response;
            appendMessage(userMessage, chatbotMessage);
        })
        .catch(error => console.error('Error:', error));
}

// function talking() {
//     audio = generate(
//     text= elevenlabsMessage,
//     voice="Bella",
//     model="eleven_multilingual_v2"
// )

// play(audio)
// }

userInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});


// const url = "https://api.thecatapi.com/v1/images/search";
// const section = document.querySelector(".container");
// const button = document.querySelector(".btn");

// button.addEventListener("click", getRandomCats);

// randomCatPhoto = (json) => {
//     let photo = json[0].url;
//     section.classList.add("cats");

//     let image = document.createElement("img");
//     image.src = photo;
//     image.classList.add("random_cats");
//     image.alt = photo;
//     section.appendChild(image);
// };

async function getRandomCats() {
    section.innerHTML = "";
    try {
        const response = await fetch(url);
        const json = await response.json();
        console.log("JSON:", json);
        return randomCatPhoto(json);
    } catch (e) {
        console.log("This is an error");
        console.log(e);
    }
}





function scrollToTargetAdjusted() {
    var element = document.getElementById('send_button');
    var headerOffset = 200;
    var elementPosition = element.getBoundingClientRect().top;
    var offsetPosition = elementPosition + window.pageYOffset - headerOffset;

    window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
    });
}


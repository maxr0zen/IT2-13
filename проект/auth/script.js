const login = 'user';
const password = 'password';

const authContainer = document.getElementById('authContainer');
const backgroundFeed = document.getElementById('backgroundFeed');


document.getElementById('login-btn').addEventListener('click', function() {
    const inputLogin = document.getElementById('login').value;
    const inputPassword = document.getElementById('password').value;
    const messageDiv = document.getElementById('message');
    
    if (inputLogin === login && inputPassword === password) {

        window.open('../feed/feed.html')
    } else {
        messageDiv.textContent = 'Неверный логин или пароль.';
        messageDiv.className = 'message error';
    }  
});
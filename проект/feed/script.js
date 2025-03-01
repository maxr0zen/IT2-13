document.addEventListener('DOMContentLoaded', function() {
    fetch('news.json')
        .then(response => response.json())
        .then(news => {
            const newsFeed = document.getElementById('news-feed');
            news.forEach(item => {
                const newsItem = document.createElement('div');
                newsItem.className = 'news-item';

                const title = document.createElement('h4');
                title.textContent = item.title;

                const content = document.createElement('p');
                content.textContent = item.content;

                const image = document.createElement('img');
                image.src = item.image;
                image.alt = item.title;

                const newsActions = document.createElement('div');
                newsActions.className = 'news-actions';

                const likeButton = document.createElement('button');
                likeButton.className = 'like-btn';
                likeButton.innerHTML = '<span class="like-icon">❤️</span><span class="like-count">0</span>';
                likeButton.onclick = function() { toggleLike(this); };

                const commentButton = document.createElement('button');
                commentButton.className = 'comment-btn';
                commentButton.textContent = '💬 Комментировать';
                commentButton.onclick = function() { toggleCommentBox(this); };

                newsActions.appendChild(likeButton);
                newsActions.appendChild(commentButton);

                const commentSection = document.createElement('div');
                commentSection.className = 'comment-section';

                const comments = document.createElement('div');
                comments.className = 'comments';

                const commentBox = document.createElement('div');
                commentBox.className = 'comment-box hidden';
                commentBox.innerHTML = '<textarea placeholder="Напишите комментарий..."></textarea><button class="btn" onclick="addComment(this)">Отправить</button>';

                commentSection.appendChild(comments);
                commentSection.appendChild(commentBox);

                const timestamp = document.createElement('small');
                timestamp.textContent = item.timestamp;

                newsItem.appendChild(title);
                newsItem.appendChild(content);
                newsItem.appendChild(image);
                newsItem.appendChild(newsActions);
                newsItem.appendChild(commentSection);
                newsItem.appendChild(timestamp);

                newsFeed.appendChild(newsItem);
            });
        })
        .catch(error => console.error('Ошибка загрузки новостей:', error));
});

function toggleLike(button) {
    const likeCount = button.querySelector('.like-count');
    let count = parseInt(likeCount.textContent);
    likeCount.textContent = count + 1;
}

function toggleCommentBox(button) {
    const commentBox = button.closest('.news-item').querySelector('.comment-box');
    commentBox.classList.toggle('hidden');
}

function addComment(button) {
    const textarea = button.previousElementSibling;
    const commentText = textarea.value.trim();
    if (commentText) {
        const commentsDiv = button.closest('.comment-section').querySelector('.comments');
        const newComment = document.createElement('div');
        newComment.textContent = commentText;
        commentsDiv.appendChild(newComment);
        textarea.value = '';
    }
}

function toggleLike(button) {
    const likeIcon = button.querySelector('.like-icon');
    const likeCount = button.querySelector('.like-count');

    if (button.classList.contains('liked')) {
        likeIcon.textContent = '❤️';
        likeCount.textContent = parseInt(likeCount.textContent) - 1;
    } else { 
        likeIcon.textContent = '❤️';
        likeCount.textContent = parseInt(likeCount.textContent) + 1;
        likeIcon.style.transform = 'scale(1.2)';
        setTimeout(() => {
            likeIcon.style.transform = 'scale(1)';
        }, 200);
    }
    button.classList.toggle('liked');
}


function toggleCommentBox(button) {
    const commentBox = button.closest('.news-item').querySelector('.comment-box');
    commentBox.classList.toggle('hidden');
}

// Добавление комментария
function addComment(button) {
    const commentBox = button.closest('.comment-box');
    const textarea = commentBox.querySelector('textarea');
    const commentText = textarea.value.trim();

    if (commentText) {
        const commentsSection = commentBox.previousElementSibling;
        const commentElement = document.createElement('div');
        commentElement.classList.add('comment');
        commentElement.textContent = commentText;
        commentsSection.appendChild(commentElement);
        textarea.value = ''; // Очищаем поле ввода
    }
}

document.getElementById('user-btn').addEventListener('click',function() {
    window.open('../user/user.html')
})

document.getElementById('user-btn').addEventListener('click',function() {
    
})

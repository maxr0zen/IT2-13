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
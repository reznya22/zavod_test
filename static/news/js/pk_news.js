let offset = 0;
const limit = 1;
const url = new URL(window.location.href);
const pathname = url.pathname;
const pk = pathname.slice(1, -1).split('/').pop();


function likeNews(newsId) {
    fetch(`/api/news/likes/${newsId}/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'id': newsId
        })
    })
    .then(response => response.json())
    .then(data => {
        updateLikesCount(newsId, data.likes);
    })
    .catch(error => console.error('Error liking news:', error));
};

function updateLikesCount(newsId, likes) {
    const likesCountElement = document.getElementById(`news-${newsId}-likes`);
    likesCountElement.textContent = likes;
};


function dislikeNews(newsId) {
    fetch(`/api/news/dislikes/${newsId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        updateDislikesCount(newsId, data.dislikes);
    })
    .catch(error => console.error('Error disliking news:', error));
}

function updateDislikesCount(newsId, dislikes) {
    const dislikesCountElement = document.getElementById(`news-${newsId}-dislikes`);
    dislikesCountElement.textContent = dislikes;
}


function loadNews() {
    fetch(`/api/news/${pk}/`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        const newsContainer = document.getElementById('news-container');

        const newsCard = document.createElement('div');
        newsCard.className = 'news-card border border-4 border-dark rounded';

        const newsContent = document.createElement('div');
        newsContent.className = 'news-content';

        newsContent.innerHTML = `
            <div class="news-wrapper">
                <div class="news-title">
                    <h3>${data.title}</h3>
                    <p>${data.text}</p>
                </div>
                <div class="news-image">
                    <img src=${data.image} alt="Photo" width="300" height="200">
                </div>
            </div>
            <div class="feedback">
                <button onclick="likeNews(${data.id})" class="btn btn-dark">Like</button>
                <span>Likes: <span id="news-${data.id}-likes">${data.likes}</span></span>
                <button onclick="dislikeNews(${data.id})" class="btn btn-dark ml-3">Dislike</button>
                <span>Dislikes: <span id="news-${data.id}-dislikes">${data.dislikes}</span></span>
            </div>
        `;

        newsCard.appendChild(newsContent);

        newsContainer.appendChild(newsCard);
    })
    .catch(error => console.error('There was a problem with the fetch operation:', error));
}

loadNews();

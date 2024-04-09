let offset = 0;
const limit = 3;
const loadedNewsIds = [];
const url = new URL(window.location.href);
const pathname = url.pathname;
const tag = decodeURI(pathname.slice(1, -1).split('/').pop());

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
    fetch(`/api/tag-news/${tag}/?offset=${offset}&limit=${limit}`)
        .then(response => response.json())
        .then(data => {
            const newsContainer = document.getElementById('news-container');
            data.forEach((news) => {
                if (!loadedNewsIds.includes(news.id)) {
                const newsCard = document.createElement('div');
                newsCard.className = 'news-card border border-4 border-dark rounded';

                const newsContent = document.createElement('div');
                newsContent.className = 'news-content';
               newsContent.innerHTML = `
                    <div class="news-wrapper">
                        <div class="news-title">
                            <h3>${news.title}</h3>
                            <p>${news.text}</p>
                        </div>
                        <div class="news-image">
                            <img src=${news.image} alt="Photo" width="300" height="200">
                        </div>
                    </div>
                    <div class="feedback">
                        <button onclick="likeNews('${news.id}')" class="btn btn-dark">Like</button>
                        <span>Likes: <span id="news-${news.id}-likes">${news.likes}</span></span>
                        <button onclick="dislikeNews('${news.id}')" class="btn btn-dark ml-3">Dislike</button>
                        <span>Dislikes: <span id="news-${news.id}-dislikes">${news.dislikes}</span></span>
                    </div>

               `;

                newsCard.appendChild(newsContent);
                newsContainer.appendChild(newsCard);
                loadedNewsIds.push(news.id);
                }
            });
            offset += limit;
        })
        .catch(error => console.error('There was a problem with the fetch operation:', error));
}

window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        loadNews();
        offset += limit;
    }
});

loadNews();

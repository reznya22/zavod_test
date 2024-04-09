from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from news import views

urlpatterns = [
    # api
    path('api/news/', views.NewsListCreateAPIView.as_view(),
         name='api-news'),
    path('api/news/<int:pk>/', views.NewsAPIView.as_view(),
         name='api-news-pk'),
    path('api/tag-news/<str:tag>/', views.TagsNewsAPIView.as_view(),
         name='api-tag-news'),
    path('api/news/statistic/', views.NewsStatisticAPIView.as_view(),
         name='api-statistic'),
    path('api/news/likes/<int:pk>/', views.NewsLikeAPIView.as_view(),
         name='api-likes'),
    path('api/news/dislikes/<int:pk>/', views.NewsDislikeAPIView.as_view(),
         name='api-dislikes'),
    # front
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.pk_news, name='pk-news'),
    path('tag-news/<str:tag>/', views.tag_news, name='tag-news'),
    path('news/statistic/', views.statistic_news, name='statistic_news'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

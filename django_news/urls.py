
from django.contrib import admin
from django.urls import path, include
from news.urls import urlpatterns as news_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += news_urls

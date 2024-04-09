import pdb

from django.db.models import F
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer, NewsStatisticSerializer


#api
class NewsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        offset = int(self.request.GET.get('offset', 0))
        limit = int(self.request.GET.get('limit', 3))
        queryset = News.objects.all()[offset:offset + limit]

        return queryset


class NewsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        if self.request.method == 'GET':
            (News.objects.filter(id=self.kwargs.get('pk'))
             .update(views_count=F('views_count')+1))
        return queryset


class TagsNewsAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.filter(tags__name=self.kwargs.get('tag'))
        return queryset


class NewsStatisticAPIView(generics.ListAPIView):
    serializer_class = NewsStatisticSerializer
    queryset = News.objects.all()


class NewsLikeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            news = News.objects.get(id=self.kwargs.get('pk'))
            news.likes += 1
            news.save()
            serializer = NewsSerializer(news)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response({"error": "News not found"}, status=status.HTTP_404_NOT_FOUND)


class NewsDislikeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            news = News.objects.get(id=self.kwargs.get('pk'))
            news.dislikes += 1
            news.save()
            serializer = NewsSerializer(news)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response({"error": "News not found"}, status=status.HTTP_404_NOT_FOUND)


# front
def news(request):
    return render(request, 'news_list.html')


def pk_news(request, pk):
    return render(request, 'pk_news.html')


def tag_news(request, tag):
    return render(request, 'tag_news.html')


def statistic_news(request):
    return render(request, 'statistic_news.html')

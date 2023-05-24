from django.shortcuts import render
from .serializers import NewsSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import News
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class news_home_page(APIView):
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        current_user = request.user
        create_news = News(reporter=current_user)
        serializer = NewsSerializer(create_news ,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class news_detail_page(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug, format=None):
        news = News.objects.get(slug=slug)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug, format=None):
        news = News.objects.get(slug=slug)
        current_user = request.user
        if current_user != news.reporter:
            return Response("You cannot edit someone's news")
        
        else:
            serializer = NewsSerializer(news, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"Message": "News update successful!!",
                            "data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    

    def delete(self, request, slug, format=None):
        news = News.objects.get(slug=slug)
        current_user = request.user
        if current_user != news.reporter:
            return Response("Stop it!!!")
        news.delete()
        return Response("Post has been deleted successfully!!", status=status.HTTP_204_NO_CONTENT)

    


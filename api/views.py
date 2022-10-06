from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from articles.models import Article
from .serializers import ArticleSerializer
from rest_framework import permissions

# Create your views here.


class ArticleList(ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
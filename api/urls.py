from django.urls import path
from .views import ArticleList, ArticleDetail


urlpatterns = [
	path('', ArticleList.as_view()),
	path('<int:pk>', ArticleDetail.as_view())
]
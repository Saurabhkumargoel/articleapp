from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

	
    path('article/create/', views.ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', views.ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', views.ArticleDelete.as_view(), name='article_delete'),
]

from django.urls import path
from . import views

app_name = 'news_blog'
urlpatterns = [
path('', views.news_post, name='news'),
path('<str:slug>/', views.post_page, name='post_detail'),
#path('tags/', views.tags_list, name='tag_post'),
]
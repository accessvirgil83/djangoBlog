from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
path('', views.gallery_post, name='gallery'),
path('<str:slug>/', views.post_page, name='gallery_detail'),
#path('tags/', views.tags_list, name='tag_post'),
]
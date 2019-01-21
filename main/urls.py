from django.urls import path
from . import views

app_name = 'main_blog'
urlpatterns = [
path('', views.main, name='main'),
#path('tags/', views.tags_list, name='tag_post'),
]
from django.urls import path
from . import views

app_name = 'service_blog'
urlpatterns = [
path('', views.service_post, name='service'),
path('<str:slug>/', views.post_service, name='service_detail'),
#path('tags/', views.tags_list, name='tag_post'),
]
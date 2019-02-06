"""WL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import staticfiles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news_blog.urls')),
    path('service/', include('service_blog.urls')),
    path('', include('main.urls')),
    path('gallery', include('gallery.urls')),
    path('search', include('search.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contacts.urls')),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'news_blog.views.handler404'
handler500 = 'news_blog.views.handler500'

handler404_1 = 'service_blog.views.handler404'
handler500_1 = 'service_blog.views.handler500'

handler404_2 = 'main.views.handler404'
handler500_2 = 'main.views.handler500'

handler404_3 = 'gallery.views.handler404'
handler500_3 = 'gallery.views.handler500'

handler404_4 = 'about.views.handler404'
handler500_4 = 'about.views.handler500'

handler404_5 = 'contacts.views.handler404'
handler500_5 = 'contacts.views.handler500'
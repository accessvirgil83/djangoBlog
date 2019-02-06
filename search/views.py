from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from news_blog.models import news_page
from service_blog.models import service_page
from gallery.models import gallery_page

from django.db.models import Q


def post(request):
	search_query = request.GET.get('search','')
	if search_query:
		post = news_page.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
		serv = service_page.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
		gal = gallery_page.objects.filter(Q(title__icontains=search_query))
	else:
		post = news_page.objects.filter(visible=1)
		serv = service_page.objects.filter(visible=1)
		gal = gallery_page.objects.filter()
	return render(request,'search/detail.html', {'post':post,'serv':serv,'gal':gal})

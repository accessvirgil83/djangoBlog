from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from  news_blog.models import news_page
from  service_blog.models import service_page


def main(request): 
	postp = news_page.objects.filter(date_news__isnull=False).latest('date_news')
	servp = service_page.objects.filter(date_news__isnull=False).latest('date_news')
	return render(request,'main/head.html', context={'post':postp,
												 		'serv':servp})





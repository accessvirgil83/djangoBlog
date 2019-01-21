from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import service_page


def service_post(request):
	post = service_page.objects.filter(visible=1)
	paginator = Paginator(post, 10)
	page = request.GET.get('page')
	postp = paginator.get_page(page)
	return render(request,'service/detail.html', {'post':postp})

def post_service(request, slug=None):
	#post_news=news_page.objects.get(slug__iexact=slug)
	post_news=get_object_or_404(service_page, slug=slug)
	return render(request,'service/list.html',context={'service_news':post_news})
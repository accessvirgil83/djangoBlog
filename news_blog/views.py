from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import news_page


def news_post(request):
	post = news_page.objects.filter(visible=1)
	paginator = Paginator(post, 10)
	page = request.GET.get('page')
	postp = paginator.get_page(page)
	return render(request,'post/detail.html', {'post':postp})

def post_page(request, slug=None):
	#post_news=news_page.objects.get(slug__iexact=slug)
	post_news=get_object_or_404(news_page, slug=slug)
	return render(request,'post/list.html',context={'post_news':post_news})
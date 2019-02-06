from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import gallery_page


def gallery_post(request):
	post = gallery_page.objects.filter()
	paginator = Paginator(post, 10)
	page = request.GET.get('page')
	postp = paginator.get_page(page)
	return render(request,'gallery/detail.html', {'gal':postp})

def post_page(request, slug=None):
	#post_news=gallery_page.objects.get(slug__iexact=slug)
	post_gallery=get_object_or_404(gallery_page, slug=slug)
	return render(request,'gallery/list.html',context={'post_gallery':post_gallery})

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
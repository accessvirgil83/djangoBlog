from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import about_page

def about_post(request):
	post = about_page.objects.filter()
	paginator = Paginator(post, 10)
	page = request.GET.get('page')
	postp = paginator.get_page(page)
	return render(request,'about/detail1.html', {'post':postp})


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
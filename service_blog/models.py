from django.db import models

from django.shortcuts import reverse

class service_page(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок")
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField(upload_to='service_image/%Y/%m/%d/', blank=True, verbose_name="Изображение услуги 1")
	image1 = models.ImageField(upload_to='service_image/%Y/%m/%d/', blank=True, verbose_name="Изображение услуги 2")
	image2 = models.ImageField(upload_to='service_image/%Y/%m/%d/', blank=True, verbose_name="Изображение услуги 3")
	image3 = models.ImageField(upload_to='service_image/%Y/%m/%d/', blank=True, verbose_name="Изображение услуги 4")
	body = models.TextField(max_length=512, verbose_name="Содержание")
	visible = models.BooleanField(default=1)
	date_news = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_news',]
	 	verbose_name = 'Услуга'
	 	verbose_name_plural = 'Услуги'
	 	

	def get_absolute_url(self):
	 	return reverse('service_blog:service_detail',kwargs={'slug': self.slug})	
	
#class Tag(models.Model):
	#title = models.CharField(max_length=50)
	#slug = models.SlugField(max_length=50, unique=True)

	
from django.db import models

from django.shortcuts import reverse

class gallery_page(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок")
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True, verbose_name="Изображение")
	image1 = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True, verbose_name="Изображение1")
	image2 = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True, verbose_name="Изображение2")
	image3 = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True, verbose_name="Изображение3")
	date_gallery = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_gallery',]
	 	verbose_name = 'Публикация'
	 	verbose_name_plural = 'Публикации'
	 	

	def get_absolute_url(self):
	 	return reverse('gallery:gallery_detail',kwargs={'slug': self.slug})	
	
#class Tag(models.Model):
	#title = models.CharField(max_length=50)
	#slug = models.SlugField(max_length=50, unique=True)

	def __str__(self):
			return '{}'.format(self.title)


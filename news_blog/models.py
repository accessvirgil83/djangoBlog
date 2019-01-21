from django.db import models

from django.shortcuts import reverse

class news_page(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок")
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField(upload_to='news_image/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
	body = models.TextField(max_length=256, verbose_name="Содержание")
	visible = models.BooleanField(default=1)
	date_news = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_news',]
	 	verbose_name = 'Публикация'
	 	verbose_name_plural = 'Публикации'
	 	

	def get_absolute_url(self):
	 	return reverse('news_blog:post_detail',kwargs={'slug': self.slug})	
	
#class Tag(models.Model):
	#title = models.CharField(max_length=50)
	#slug = models.SlugField(max_length=50, unique=True)

	def __str__(self):
			return '{}'.format(self.title)

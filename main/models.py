from django.db import models
from django.shortcuts import reverse

# Create your models here.
class ImgNav(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок слайдера")
	image1 = models.ImageField(upload_to='nav_image/%Y/%m/%d/', blank=True, verbose_name="Изображение товара 1")
	image2 = models.ImageField(upload_to='nav_image/%Y/%m/%d/', blank=True, verbose_name="Изображение товара 2")
	image3 = models.ImageField(upload_to='nav_image/%Y/%m/%d/', blank=True, verbose_name="Изображение товара 3")
	date_img = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")	

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_img']
	 	verbose_name = 'Изображение'
	 	verbose_name_plural = 'Изображения'


class About(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок о нас")
	image1 = models.ImageField(upload_to='about_image/%Y/%m/%d/', blank=True, verbose_name="Изображение о нас 1")
	image2 = models.ImageField(upload_to='about_image/%Y/%m/%d/', blank=True, verbose_name="Изображение о нас 2")
	body = models.TextField(max_length=256, verbose_name="Содержание")
	date_about = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_about']
	 	verbose_name = 'О Нас'
	 	verbose_name_plural = 'О Нас'


class Contacts(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок контакты")
	image1 = models.ImageField(upload_to='contacts_image/%Y/%m/%d/', blank=True, verbose_name="Изображение контакты 1")
	image2 = models.ImageField(upload_to='contacs_image/%Y/%m/%d/', blank=True, verbose_name="Изображение контакты 2")
	body = models.TextField(max_length=256, verbose_name="Содержание")
	date_contact = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_contact']
	 	verbose_name = 'Контакт'
	 	verbose_name_plural = 'Контакты'


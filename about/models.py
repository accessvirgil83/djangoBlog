from django.db import models


class about_page(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок")
	image = models.ImageField(upload_to='about_image/%Y/%m/%d/', blank=True, verbose_name="Изображение о нас")
	body = models.TextField(max_length=256, verbose_name="Содержание")
	date_about = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_about',]
	 	verbose_name = 'Информация'
	 	verbose_name_plural = 'Информации'
# Create your models here.

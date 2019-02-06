from django.db import models

class contact_page(models.Model):
	title = models.CharField(max_length=128, db_index=True, verbose_name="Заголовок")
	image = models.ImageField(upload_to='contacts_image/%Y/%m/%d/', blank=True, verbose_name="Изображение контакты")
	body = models.TextField(max_length=256, verbose_name="Содержание")
	email = models.CharField(max_length=128, db_index=True, verbose_name="mail")
	date_contact = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

	def __str__(self):
			return '{}'.format(self.title)

	class Meta:
	 	ordering = ['-date_contact',]
	 	verbose_name = 'Контакт'
	 	verbose_name_plural = 'Контакты'

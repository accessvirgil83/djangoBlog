# Generated by Django 2.1.3 on 2019-01-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='news_image/%Y/%m/%d/', verbose_name='Изображение товара')),
                ('body', models.TextField(max_length=256, verbose_name='Содержание')),
                ('visible', models.BooleanField(default=1)),
                ('date_news', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['-date_news'],
            },
        ),
    ]

from django.contrib import admin
from .models import news_page

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "slug","image", "body", "date_news"]
    list_display_links = ["id", "date_news"]
    list_editable = ["title"]
    list_filter = ["date_news"]
    search_fields = ["title", "body"]
    class Meta:
        model = news_page

admin.site.register(news_page, PostModelAdmin)
from django.contrib import admin
from .models import service_page

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "slug","image","image1","image2","image3", "body", "date_news"]
    list_display_links = ["id", "date_news"]
    list_editable = ["title"]
    list_filter = ["date_news"]
    search_fields = ["title", "body"]
    class Meta:
        model = service_page

admin.site.register(service_page, PostModelAdmin)


from django.contrib import admin
from .models import gallery_page

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "slug","image", "image1", "image2", "image3", "date_gallery"]
    list_display_links = ["id", "date_gallery"]
    list_editable = ["title"]
    list_filter = ["date_gallery"]
    search_fields = ["title"]
    class Meta:
        model = gallery_page

admin.site.register(gallery_page, PostModelAdmin)
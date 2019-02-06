from django.contrib import admin
from .models import about_page

class AboutModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title","image", "body", "date_about"]
    list_display_links = ["id", "date_about"]
    list_editable = ["title"]
    list_filter = ["date_about"]
    search_fields = ["title", "body"]
    class Meta:
        model = about_page

admin.site.register(about_page, AboutModelAdmin)

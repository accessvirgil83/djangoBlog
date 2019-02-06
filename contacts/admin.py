from django.contrib import admin
from .models import contact_page

class AboutModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title","image", "body","email", "date_contact"]
    list_display_links = ["id", "date_contact"]
    list_editable = ["title"]
    list_filter = ["date_contact"]
    search_fields = ["title", "body"]
    class Meta:
        model = contact_page

admin.site.register(contact_page, AboutModelAdmin)


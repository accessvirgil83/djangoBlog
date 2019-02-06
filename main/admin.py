from django.contrib import admin
from .models import ImgNav
class ContactsModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "image1", "image2", "image3", "date_img"]
    list_display_links = ["id", "date_img"]
    list_editable = ["title"]
    list_filter = ["date_img"]
    search_fields = ["title"]
    class Meta:
        model = ImgNav

admin.site.register(ImgNav, ContactsModelAdmin)
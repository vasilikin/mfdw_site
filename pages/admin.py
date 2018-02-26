from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','updatedate')
    ordering=('title',)
    search_fields = ('title',)

admin.site.register(Page, PageAdmin)

# Register your models here.

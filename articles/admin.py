from django.contrib import admin

# Register your models here.
from .models import Articles,text
class text_manager(admin.ModelAdmin):
    list_display = ['title','article']
    list_editable = ['article']
    list_filter = ['article']




admin.site.register(Articles)
admin.site.register(text,text_manager)
from django.contrib import admin

# Register your models here.
from .models import Articles, text, Tags,Catagorizes


class text_manager(admin.ModelAdmin):
    list_display = ['title','article']
    list_editable = ['article']
    list_filter = ['article']



class tag_manager(admin.ModelAdmin):
    list_display = ['tag']
    # list_editable = ['tag']
    list_filter = ['tag']


class Articles_manager(admin.ModelAdmin):
    list_display = ['title','catagorize']
    list_editable = ['catagorize']




admin.site.register(Articles,Articles_manager)
admin.site.register(Catagorizes)
admin.site.register(text,text_manager)
admin.site.register(Tags,tag_manager)
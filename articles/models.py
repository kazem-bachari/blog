from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q


class Catagorizes(models.Model):
    catagorizes = models.CharField(max_length=40, verbose_name='تگ')
    def __str__(self):
       return self.catagorizes
    class Meta:
        verbose_name = ' دسته بندی'
        verbose_name_plural = "دسته بندی ها"


class Articles_manager(models.Manager):
    def search(self,query):
        lookup=Q(title__contains=query)|Q(tags__tag=query)|Q(catagorize__catagorizes=query)
        return self.get_queryset().filter(lookup).distinct()
class Articles(models.Model):
    title=models.CharField(max_length=100,verbose_name='موضوع')
    paragraph=models.TextField(verbose_name='متن ',null=False,blank=False,default=' ')
    img=models.ImageField(verbose_name='عکس')
    date=models.DateTimeField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    catagorize = models.ForeignKey(Catagorizes,on_delete=models.CASCADE,blank=True,null=True)
    objects=Articles_manager()
    def __str__(self):
       return self.title
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = "مقالات"
class text(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True,default='')
    text = models.TextField(verbose_name='پاراگراف')
    article=models.ForeignKey(Articles,null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name='پارگراف ها'
        verbose_name_plural="متن"


class comments(models.Model):
    username=models.CharField(max_length=100)
    article=models.ForeignKey(Articles,on_delete=models.PROTECT,null=False,blank=False,default=' ')
    email=models.EmailField(max_length=100)
    text=models.TextField(max_length=300)
    time=models.TimeField(auto_now_add=True)
    class Meta:
        verbose_name='نظرات'
        verbose_name_plural="نظر"
    def __str__(self):
        return self.text
class Tags(models.Model):
    tag = models.CharField(max_length=40,verbose_name='تگ')
    article=models.ManyToManyField(Articles)

    class Meta:
        verbose_name='لیست تگ'
        verbose_name_plural="تگ"


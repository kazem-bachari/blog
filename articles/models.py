from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=100,verbose_name='موضوع')
    paragraph=models.TextField(verbose_name='متن ',null=False,blank=False,default=' ')
    img=models.ImageField(verbose_name='عکس')
    date=models.DateTimeField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
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
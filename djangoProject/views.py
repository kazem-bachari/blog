from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from articles.models import Articles, text, Tags, Catagorizes
from django.views.generic import ListView

def home(request):
    articles=Articles.objects.all().order_by('-time')
    catagorizes=Catagorizes.objects.all()
    context={
        'articles':articles[0:4],
        'catagorizes':catagorizes
    }
    print(request.user.is_superuser)
    return render(request,'index.html',context)

def Logout(request):
    logout(request)
    print(request)
    return redirect('/')
class articles(ListView):
    template_name = 'articles.html'
    paginate_by = 4
    def get_queryset(self):
        return Articles.objects.all()
def article_detaile(request,number):
    article=Articles.objects.filter(id=number).first()
    all_text=article.text_set.all()
    all_tags=article.tags_set.all()
    category=article.catagorize.catagorizes
    similar_articles=Articles.objects.filter(catagorize__catagorizes=category).exclude(id=number).distinct()
    context={
        'article':article,
        'all_text':all_text,
        'all_tags':all_tags,
        'similar_articles':similar_articles,
    }
    return render(request,'article_detaile.html',context)
class search(ListView):
    template_name = 'articles.html'
    paginate_by = 4
    def get_queryset(self):
        request=self.request
        query=request.GET.get('q')
        if query is not None:
            return Articles.objects.search(query)
        else:
            return Articles.objects.all()

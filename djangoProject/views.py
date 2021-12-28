from django.shortcuts import render

from articles.models import Articles,text


def home(request):
    articles=Articles.objects.all().order_by('-time')

    context={
        'articles':articles[0:4]
    }
    return render(request,'index.html',context)

def articles(request):
    articles=Articles.objects.all()


    context={
        'articles':articles,

    }
    return render(request,'articles.html',context)

def article_detaile(request,number):
    article=Articles.objects.filter(id=number).first()
    all_text=article.text_set.all()
    print(all_text)

    context={
        'article':article,
        'all_text':all_text
    }
    return render(request,'article_detaile.html',context)
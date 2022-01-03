from django.shortcuts import render, redirect


# Create your views here.
from articles.models import Articles,text


def edit_article_page(request):
    articles = Articles.objects.all()
    if request.method=='POST':

        title = request.POST['select']
        article=Articles.objects.filter(title=title).first()
        article_text=article.text_set.all()
        select_item=article.title
        new_p=request.POST['new_text'].strip()
        new_titile=request.POST['new_title'].strip()
        for i in request.POST :
            if 'paragraph' in  i:
                item=text.objects.get(id=request.POST[i])
                item.delete()
        if len(new_p)>2:
            text.objects.create(text=new_p,article_id=article.id,title=new_titile)


    else:

        if (request.user.is_superuser):
            article = Articles.objects.all().last()
            article_text = article.text_set.all()
            select_item = article.title

        else:
            return redirect('/')
    context = {
        'articles': articles,
        'article': article,
        'article_text': article_text,
        'select_item': select_item,
    }
    return render(request, 'edit_article_page.html', context)
from django.urls import path, include

from account.views import loginForm,registerForm,Edit_information
from articles.views import edit_article_page

urlpatterns=[
    path('edit_article_page', edit_article_page),

]

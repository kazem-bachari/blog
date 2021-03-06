"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from serializers import views
from .views import home,article_detaile,articles,search,Logout
router = routers.DefaultRouter()
router.register(r'articles', views.ArticlesViewSet)
router.register(r'catagorize', views.CatagorizesViewSet)
router.register(r'text', views.TextViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',home),
    path('logout',Logout),
    path('',include("account.urls")),
    path('article/',include("articles.urls")),
    path('articles',articles.as_view()),
    path('articles/search',search.as_view()),
    path('articles/<number>',article_detaile),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions

from articles.models import Articles, Catagorizes, text
from .serializers import ArticlesSerializer, CatagorizesSerializer, TextSerializer


class ArticlesViewSet(viewsets.ModelViewSet):

    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CatagorizesViewSet(viewsets.ModelViewSet):

    queryset = Catagorizes.objects.all()
    serializer_class = CatagorizesSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TextViewSet(viewsets.ModelViewSet):
    queryset = text.objects.all()
    serializer_class = TextSerializer
    # permission_classes = [permissions.IsAuthenticated]



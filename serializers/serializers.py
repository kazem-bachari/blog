from django.contrib.auth.models import User, Group
from  rest_framework import serializers

from articles.models import Articles, Catagorizes, text


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ['title','paragraph','time','date','catagorize']
class CatagorizesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagorizes
        fields = ['catagorizes']
class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = text
        fields = ['title','text','article']

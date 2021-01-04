from django.db import models
from rest_framework import serializers
from .models import Language

# ModelSerializer & HyperlinkedModelSerializer both contains url, so what's the difference?
# The difference is when you have Groups, using ModelSerializer won't show the url 
# while using HyperlinkedModelSerializer will

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')

# class LanguageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Language
#         fields = ('id', 'url', 'name', 'paradigm')
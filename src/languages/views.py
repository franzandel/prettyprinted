from src.languages.serializers import LanguageSerializer
from src.languages.models import Language
from django.shortcuts import render
from rest_framework import viewsets

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

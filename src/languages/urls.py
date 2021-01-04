from src.languages.views import LanguageView
from django.urls import path, include
from rest_framework import routers

# Will auto generate detail, so we can go to endpoint languages/{id}
router = routers.DefaultRouter()
router.register('languages', LanguageView)

urlpatterns = [
    path('', include(router.urls))
]
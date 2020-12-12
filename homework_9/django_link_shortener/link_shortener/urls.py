from django.urls import path

from link_shortener.views import shortener

urlpatterns = [
    path('', shortener)
]

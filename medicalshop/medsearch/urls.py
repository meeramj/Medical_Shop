from django.urls import path
from .import views

app_name='medsearch'
urlpatterns = [
    path('', views.SearchResult, name='SearchResult'),
]


from . import views
from django.urls import path
app_name = 'medpurchase'
urlpatterns = [
    path('medicine/', views.medicine, name='medicine'),
    path('dist/', views.dist, name='dist'),
    path('thanks/', views.thanks, name='thanks'),

]
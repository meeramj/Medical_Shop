from django.urls import path
from . import views

app_name = 'medshop'
urlpatterns = [
    path('',views.allProdCat, name='allProdCat'),
    path('purchase/',views.purchase, name='purchase'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail, name='proCatDetail'),
]
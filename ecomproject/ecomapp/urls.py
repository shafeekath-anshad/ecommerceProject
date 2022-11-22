from . import views
from django.urls import path
app_name='ecomapp'
urlpatterns = [

    path('', views.allprodCat, name="allprodCat"),
    path('<slug:c_slug>/',views.allprodCat , name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]

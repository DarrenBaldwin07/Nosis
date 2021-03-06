from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('product/', views.product),
    path('apiData/', views.apiData),
    path('apiSymp/', views.apiSymp),
    path('symptoms/', views.symptoms),
    path('product/symptoms/', views.symptoms)
]

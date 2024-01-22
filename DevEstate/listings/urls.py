from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property_detail/<int:zpid>/', views.property_detail, name='property_detail'),
]
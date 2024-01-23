from django.urls import path

from . import views
from .views import PropertyCreateView, PropertyUpdateView
from .views import PropertyDeleteView


app_name = 'listings'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property_detail/<int:zpid>/', views.property_detail, name='property_detail'),
    path('create/', PropertyCreateView.as_view(), name='property_create'),
    path('update/<int:pk>/', PropertyUpdateView.as_view(), name='property_update'),
    path('delete/<int:pk>/', PropertyDeleteView.as_view(), name='property_delete'),
]
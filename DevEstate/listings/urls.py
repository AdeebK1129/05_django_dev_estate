from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('listings/', views.index, name='index'),
    path('listings/<int:pk>/', views.index, name='listing_detail'),
]
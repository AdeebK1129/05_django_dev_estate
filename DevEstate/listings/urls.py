from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('listings/', views.index, name='index'),
    path('listings/<int:pk>/', views.index, name='listing_detail'),
]
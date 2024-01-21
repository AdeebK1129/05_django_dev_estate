from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/main/')),
    path('main/', include('main.urls')), 
    path('listings/', include('listings.urls', namespace='listings')),
]

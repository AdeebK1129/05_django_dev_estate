from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Property

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})

from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['imgSrc', 'street_address', 'city', 'state', 'zipcode', 'country', 'living_area', 'bedrooms', 'bathrooms', 'year_built', 'price', 'description']
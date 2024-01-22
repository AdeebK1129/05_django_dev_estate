from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Property, PropertyFeatures, PropertyAgent, PropertySchool, PriceHistory, NearbyHomes

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})


def property_detail(request, zpid):
    # Get the property by zpid or return 404 if not found
    property = get_object_or_404(Property, zpid=zpid)
    
    # Get related data
    property_features = PropertyFeatures.objects.filter(property=property).first()
    property_agents = PropertyAgent.objects.filter(property=property).select_related('agent')
    property_schools = PropertySchool.objects.filter(property=property).select_related('school')
    price_history = PriceHistory.objects.filter(property=property).order_by('-date')
    nearby_homes = NearbyHomes.objects.filter(property=property)
    
    context = {
        'property': property,
        'property_features': property_features,
        'property_agents': property_agents,
        'property_schools': property_schools,
        'price_history': price_history,
        'nearby_homes': nearby_homes,
    }
    
    return render(request, 'listings/property_detail.html', context)

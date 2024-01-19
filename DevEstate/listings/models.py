from django.db import models

# Create your models here.

from django.db import models

class Property(models.Model):
    zpid = models.IntegerField(primary_key=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    living_area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    year_built = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    date_posted = models.DateTimeField()
    date_sold = models.DateTimeField(null=True, blank=True)
    home_type = models.CharField(max_length=255)
    property_tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    time_on_zillow = models.CharField(max_length=255)
    home_status = models.CharField(max_length=255)
    annual_homeowners_insurance = models.DecimalField(max_digits=19, decimal_places=2)
    rent_zestimate = models.DecimalField(max_digits=19, decimal_places=2)
    brokerage_name = models.CharField(max_length=255, null=True, blank=True)
    page_view_count = models.IntegerField()
    description = models.TextField()

class PropertyFeatures(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    flooring = models.CharField(max_length=255, null=True, blank=True)
    foundation_details = models.CharField(max_length=255, null=True, blank=True)
    accessibility_features = models.CharField(max_length=255, null=True, blank=True)
    garage_spaces = models.IntegerField(null=True, blank=True)
    parking_spaces = models.IntegerField(null=True, blank=True)
    view_type = models.CharField(max_length=255, null=True, blank=True)
    water_view = models.BooleanField(default=False)
    heating = models.CharField(max_length=255, null=True, blank=True)
    cooling = models.CharField(max_length=255, null=True, blank=True)
    construction_materials = models.CharField(max_length=255, null=True, blank=True)
    roof_type = models.CharField(max_length=255, null=True, blank=True)
    lot_size = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    hoa_fee = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)

class Agent(models.Model):
    display_name = models.CharField(max_length=255)
    review_count = models.IntegerField()
    rating_average = models.DecimalField(max_digits=3, decimal_places=2)
    phone_number = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    badge_type = models.CharField(max_length=255)

class PropertyAgent(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

class School(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    students_per_teacher = models.IntegerField()
    size = models.IntegerField()
    level = models.CharField(max_length=255)
    grades = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=5, decimal_places=2)

class PropertySchool(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class PriceHistory(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date = models.DateTimeField()
    event = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    price_per_square_foot = models.DecimalField(max_digits=19, decimal_places=2)

class NearbyHomes(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    zpid = models.IntegerField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    home_type = models.CharField(max_length=255)
    home_status = models.CharField(max_length=255)
from django.db import models

class HouseListing(models.Model):
    zpid = models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    living_area = models.PositiveIntegerField()
    lot_size = models.CharField(max_length=20)
    description = models.TextField()
    short_sale = models.BooleanField(default=False)
    year_built = models.PositiveIntegerField()
    heating = models.CharField(max_length=100)
    cooling = models.CharField(max_length=100, null=True, blank=True)
    parking_spaces = models.PositiveIntegerField()
    days_on_zillow = models.PositiveIntegerField()
    price_per_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    offer_review_date = models.DateTimeField(null=True, blank=True)
    list_date = models.DateField()
        
    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zipcode}"

import http.client
import json
import ssl
import secrets
from datetime import datetime
from listings.models import HouseListing
from django.shortcuts import render


class ZillowApiClient:
    def __init__(self, api_key, api_host):
        self.api_key = api_key
        self.api_host = api_host

    def fetch_data(self, url):
        conn = http.client.HTTPSConnection(self.api_host)
        headers = {
            'X-RapidAPI-Key': self.api_key,
            'X-RapidAPI-Host': self.api_host
        }
        conn.request("GET", url, headers=headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def fetch_all_data(api_client, url):
    return api_client.fetch_data(url)

def fetch_individual_data(api_client, zpid):
    url = f"/property?zpid={zpid}"
    return api_client.fetch_data(url)

def create_house_listing(data):
    HouseListing.objects.create(**data)

def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    api_client = ZillowApiClient(api_key=secrets.key, api_host=secrets.host)
    url = "/searchByUrl?url=https://www.zillow.com/new-york-ny/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-74.15820883203124%2C%22east%22%3A-73.66382406640624%2C%22south%22%3A40.57279370530749%2C%22north%22%3A40.93585324525284%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
    
    listingsInfo = json.loads(fetch_all_data(api_client, url))

    for i in range(len(listingsInfo["props"])):
        zpid = listingsInfo["props"][i]["zpid"]
        individual_data = json.loads(fetch_individual_data(api_client, zpid))
        
        house_data = {
            'zpid': zpid,
            'address': individual_data.get('address', ''),
            'city': individual_data.get('city', ''),
            'state': individual_data.get('state', ''),
            'zipcode': individual_data.get('zipcode', ''),
            'price': individual_data.get('price', 0),
            'bedrooms': individual_data.get('bedrooms', 0),
            'bathrooms': individual_data.get('bathrooms', 0),
            'living_area': individual_data.get('living_area', 0),
            'lot_size': individual_data.get('lot_size', ''),
            'description': individual_data.get('description', ''),
            'short_sale': individual_data.get('short_sale', False),
            'year_built': individual_data.get('year_built', 0),
            'heating': individual_data.get('heating', ''),
            'cooling': individual_data.get('cooling', None),
            'parking_spaces': individual_data.get('parking_spaces', 0),
            'days_on_zillow': individual_data.get('days_on_zillow', 0),
            'price_per_sqft': individual_data.get('price_per_sqft', 0),
            'offer_review_date': datetime.fromisoformat(individual_data.get('offer_review_date')) if individual_data.get('offer_review_date') else None,
            'list_date': datetime.fromisoformat(individual_data.get('list_date')) if individual_data.get('list_date') else None,
        }

        create_house_listing(house_data)

if __name__ == "__main__":
    main()

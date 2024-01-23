# 05_django_real_estate
Adeeb Khan, John Chandler III, Jason Lei, Samuel Li

------WARNING-------

With this project, we have chosen to pay for an API called Zillow.com ourselves. We have been given a monthly limit of 13,000 Requests, and are limited to 2 Requests per Second.
Please be careful with your requests!! I do not have enough money to pay a bajillion dollars for exceeding the limit :(

In this project, we utilize the Zillow.com API as the basis of our listings pages.
In order to use the API, we followed these steps:
1. Established a connection to the SearchByURL endpoint of our API  in order to obtain a list of properties in New York City
2. Return the Data from that connection and convert it into a Json Object so that we can parse it
3. Iterate through the JSON object, looking for each property's ZPID
4. Once found, use the ZPID to send another request to the /properties endpoint of our API in order to obtain data specific to that listing
For the sake of safety and because we are paying for our API access, we have used .git ignore to hide our API host and key from public viewers. If necessary, we can email you our key.

----------PROJECT SETUP INSTRUCTIONS------------------
1. Go to insights -> network -> tip of adeeb branch and clone the repo (this is because there have been some serious errors revolving around git which has left our primary branch to become adeeb. We have also had difficulties merging adeeb into main)
2. Set up virtual environment 
3. Install psycopg2, django onto the virtual environment if not already installed. If psycopg2 fails, try the binary version. 
4. Create secrets.json file in DevEstate app and enter in your database information
5. Create api_secrets file in the notebooks directory and include the key and host we emailed to you
key = “”
host = “”
6. Open api.ipynb in the notebooks folder and run through each cell individually. This will populate your models. ***
7. Make migrations and migrate
8. Run the server and go through the website 

Some Key Notes:

***You will notice the propertylist.py module file within notebooks. This file contains an array of 40 objects obtained from our API through API calls. We have this hardcoded to ensure that our API does not exceed its limit which will cause us to pay money. If you do want to actually test the API and what we called you will be modifying some of the cells in the api.ipynb:

Currently the save_properties_and_related_data method takes in the hard coded propertylist module to save API requests. 

This line is:

property_dictionary_list = propertylist.property_dictionary_list

You can instead change this to be

property_dictionary_list = parseListings(listingsInfo) 

This will then individually make calls to the API (this will return many print statements), before finally populating your models. 





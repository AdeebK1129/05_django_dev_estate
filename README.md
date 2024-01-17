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


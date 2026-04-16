import requests 
import json
#import http.client


# response status code
# send GET request to API endpoint 
# code 
response = requests.get("http://api.open-notify.org/this-api-doesn't-exist")     # retrieve data from api
print(response.status_code)

response1 = requests.get("http://api.open-notify.org/astros.json")
print(response1.status_code)        # error handling 

print(response1.json())   # convert API reponses into dictionaries using .json()
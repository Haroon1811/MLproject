# chcek difference between patch , post and put methoda from requests library 
import json
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# assign headers --- for github api
headers = {'Accept':'application/vnd.github.v3+json'}
response = requests.get(url, headers = headers)
print(f"Status code : {response.status_code}")

# store api response to a varaible 
r_dict = response.json()

print(r_dict.values())

import json
import requests 
import pandas as pd

url = 'https://api.example.com/countries'
url2 = 'https://restcountries.com/v3.1/region/asia'
params = {
    'fields' : 'name, currencies'
}
r = requests.get(url2, params = params)

filtered_data = r.json()

#print(filtered_data)

df = pd.DataFrame(filtered_data)
print(df.head(12))
import requests 
url = "https://raw.githubusercontent.com/Haroon1811/MLproject/main/new.py"
response = requests.get(url)
print(response.text)
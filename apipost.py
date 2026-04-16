import json 
import requests 
url = 'https://jsonplaceholder.typicode.com/posts'
# data to be sent 
new = {'userId':1,
       'id' : 11,
       'title':'A new post for the website',
       'body': 'Content of the post'
       }

r = requests.post(url, json=new)
print(r.json())
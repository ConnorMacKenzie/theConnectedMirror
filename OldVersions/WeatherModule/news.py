import json
import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=cc475626d985425e97c6eaf76f800e6d')

r = requests.get(url)
data = json.loads(r.text)

articles = data['articles']

for i in articles:
    print (i['title'] + "\n" + i['description'] + "\n\n")
    

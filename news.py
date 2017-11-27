import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey={5fada885b0fc446a808d12b8f74e863e}')

r = requests.get(url)

print (r.json)



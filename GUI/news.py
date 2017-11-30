import json, requests, socket, sys, time

class newsData:

    def __init__(self):
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=bbc-news&'
               'apiKey=cc475626d985425e97c6eaf76f800e6d')

        r = requests.get(url)
        data = json.loads(r.text)

        self.articles = data['articles']



    def serializable(self):
        return self.__dict__

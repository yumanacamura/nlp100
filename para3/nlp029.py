from  nlp028 import dic
import json
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
with urllib.request.urlopen('https://en.wikipedia.org/w/api.php?action=query&titles=FILE:{0}&prop=imageinfo&iiprop=url&format=json'.format(dic['国旗画像']).replace(' ','%20')) as res:
    url = json.loads(res.read().decode('utf-8'))['query']['pages']['23473560']['imageinfo'][0]['url']
print(url)

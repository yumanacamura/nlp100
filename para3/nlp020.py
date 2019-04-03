import gzip,json
filename = 'jawiki-country.json.gz'

f = gzip.open(filename)
wiki = f.readlines()
f.close()

eng=None

for l in wiki:
    article = json.loads(l)
    if article['title']=='イギリス':
        eng = article
if __name__ == '__main__':
    print(eng['text'])

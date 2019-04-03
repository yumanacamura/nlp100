import pickle
filename = 'neko.pickle'

with open(filename,'rb') as f:
    morpheme = pickle.load(f)
nouns=set()
for r in morpheme:
    i = 0
    n = len(r)-1
    while i<n:
        cnt = 0
        tmp = ''
        while i<len(r) and r[i]['pos']=='名詞':
            tmp+=r[i]['surface']
            i+=1
            cnt+=1
        if cnt>1:
            nouns.add(tmp)
        i+=1
print('\n'.join(nouns))

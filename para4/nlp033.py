import pickle
filename = 'neko.pickle'

with open(filename,'rb') as f:
    morpheme = pickle.load(f)
nouns=set()
for r in morpheme:
    for w in r:
        if w['pos']=='名詞' and w['pos1']=='サ変接続':
            nouns.add(w['surface'])
print('\n'.join(nouns))

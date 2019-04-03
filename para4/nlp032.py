import pickle
filename = 'neko.pickle'

with open(filename,'rb') as f:
    morpheme = pickle.load(f)
verbs=set()
for r in morpheme:
    for w in r:
        if w['pos'] == '動詞':
            verbs.add(w['base'])
print('\n'.join(verbs))

import pickle
filename = 'neko.pickle'

with open(filename,'rb') as f:
    morpheme = pickle.load(f)
nouns=set()
for r in morpheme:
    for i in range(len(r)-2):
        if r[i]['pos']=='名詞' and r[i+1]['surface']=='の' and r[i+2]['pos']=='名詞':
            nouns.add('{0}の{1}'.format(r[i]['surface'],r[i+2]['surface']))
print('\n'.join(nouns))

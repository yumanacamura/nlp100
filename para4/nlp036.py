from collections import Counter
import pickle
filename = 'neko.pickle'

with open(filename,'rb') as f:
    morpheme = pickle.load(f)

freq = Counter()
for r in morpheme:
    for w in r:
        freq[w['surface']]+=1
freq = freq.most_common()
if __name__ == '__main__':
    print(freq)

import pickle
filename = 'neko.txt.mecab'
save_flg = False
f = open(filename, 'r')
morpheme =[[(lambda e:{'surface':e[0], 'base':e[7], 'pos':e[1], 'pos1':e[2]})
(word.replace('\t',',').split(',')) for word in raw.split('\n') if word]
 for raw in f.read().split('EOS\n')]
f.close()
if save_flg:
    with open('neko.pickle','wb') as f:
        pickle.dump(morpheme,f)
if __name__ == '__main__':
     print(morpheme)

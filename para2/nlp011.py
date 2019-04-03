filename='hightemp.txt'
with open(filename,'r') as f:
    for r in f.readlines():
        print(r.replace('\t',' '),end='')

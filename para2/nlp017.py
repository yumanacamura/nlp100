filename ='hightemp.txt'
f = open(filename,'r')
print(*set([r.split('\t')[0] for r in f.readlines()]))
f.close()

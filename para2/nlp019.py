from collections import Counter
filename ='hightemp.txt'
f = open(filename,'r')

print('\n'.join([i[0] for i in sorted(Counter([i.split('\t')[0] for i in f.readlines()]).items(),key=lambda e:-e[1])]))
f.close()

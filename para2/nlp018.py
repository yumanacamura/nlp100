filename ='hightemp.txt'
f = open(filename,'r')
print(''.join(sorted(f.readlines(),key=lambda r:r.split('\t')[2])[::-1]))
f.close()

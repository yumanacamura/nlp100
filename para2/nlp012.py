filename ='hightemp.txt'
outname = ['col1.txt','col2.txt']
f = open(filename,'r')
o = [open(on,'w') for on in outname]
for r in f.readlines():
    c = r.split('\t')
    o[0].write(c[0]+'\n')
    o[1].write(c[1]+'\n')
f.close()
o[0].close()
o[1].close()

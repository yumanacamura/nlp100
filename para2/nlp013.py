filename = ['col1.txt','col2.txt']
outfile = 'out.txt'
f = [open(fn,'r') for fn in filename]
o = open(outfile,'w')
for r in list(zip(*[[r.strip() for r in i.readlines()] for i in f])):
    o.write('{0}\t{1}\n'.format(*r))
f[0].close()
f[1].close()
o.close()

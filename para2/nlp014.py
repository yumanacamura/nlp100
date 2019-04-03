import sys
args = sys.argv
filename = 'hightemp.txt'

f = open(filename,'r')
rs = f.readlines()
for i in range(int(args[1])):
    print(rs[i],end='')
f.close()

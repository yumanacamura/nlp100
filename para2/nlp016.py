import sys
args = sys.argv
filename = 'hightemp.txt'
f = open(filename,'r')
rs = f.readlines()
nr = len(rs)
cnt = 0
for i in range(int(args[1]),0,-1):
    print(''.join(rs[cnt:cnt+nr//i])+'-'*40)
    cnt += nr//i
    nr -= nr//i

f.close()

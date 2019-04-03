import random

def shffl(w):
    if len(w)>4:
        t=[w[0],list(w[1:-1]),w[-1]]
        random.shuffle(t[1])
        w=t[0]+''.join(t[1])+t[2]
    return w

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

for w in s.split()[:-1]:
    print(shffl(w),end=' ')
print(shffl(s.split()[-1]))

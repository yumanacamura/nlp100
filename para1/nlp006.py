def ngram(l):
    return [[l[i],l[i+1]] for i in range(len(l)-1)]

x,y = ngram("paraparaparadise"),ngram("paragraph")
print('和集合:',[e for i,e in enumerate(x+y) if e not in (x+y)[:i]])
print('積集合:',[e for i,e in enumerate(x) if (e not in x[:i]) and (e in y)])
print('差集合:',[e for i,e in enumerate(x) if (e not in x[:i]) and (e not in y)])
print('"se" in X:',['s','e'] in x)
print('"se" in Y:',['s','e'] in y)

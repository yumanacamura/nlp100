def ngram(l):
    return [[l[i],l[i+1]] for i in range(len(l)-1)]

s="I am an NLPer"
print(ngram(s.split()))
print(ngram(s.replace(' ','')))

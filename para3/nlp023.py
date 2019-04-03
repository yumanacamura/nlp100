from  nlp020 import eng
import re
p = [re.compile(i) for i in [r'^={2,}','={2,}$']]
print('\n'.join(
[(lambda e:'{0} {1}'.format(i,str(e)))(p[0].search(i).span()[1])
for i in eng['text'].split('\n') if p[0].search(i) and p[1].search(i)]
))

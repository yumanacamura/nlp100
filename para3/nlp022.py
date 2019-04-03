from  nlp020 import eng
import re
p = [re.compile(i) for i in [r'^\[\[Category:', r'(\|.+)?\]\]$']]
print('\n'.join([p[1].subn('',p[0].subn('',i)[0])[0] for i in eng['text'].split('\n') if p[0].search(i) and p[1].search(i)]))

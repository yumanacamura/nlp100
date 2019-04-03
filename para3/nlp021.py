from  nlp020 import eng
import re
p = re.compile(r'\[\[Category:.+\]\]')
print('\n'.join([i for i in eng['text'].split('\n') if p.fullmatch(i)]))

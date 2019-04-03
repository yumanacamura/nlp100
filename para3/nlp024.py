from  nlp020 import eng
import re
p = re.compile(r'[^ :]+\.((jpg)|(JPG)|(png)|(PNG)|(svg)|(SVG))')
print('\n'.join(
[i[0] for i in
[p.search(i) for i in eng['text'].split('\n')]
if i]))

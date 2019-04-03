from  nlp026 import dic
import re
p = re.compile(r"\[{2}[^\]]*?([^\|\]]*)\]{2}")
for k,v in dic.items():
    dic[k] = p.subn(r'\1',v)[0]
if __name__ == '__main__':
    print('\n'.join(['{0}:{1}'.format(k,v) for k,v in dic.items()]))

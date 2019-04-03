from  nlp020 import eng
import re
p = re.compile(r'\{{2}基礎情報.*?^\}{2}$',re.DOTALL|re.MULTILINE)
dic={i[0]:i[1] for i in
[i.replace('\n',' ').split(' = ') for i in p.search(eng['text'])[0][:-3].split('\n|')[1:]]}
if __name__ == '__main__':
    print('\n'.join(['{0}:{1}'.format(k,v) for k,v in dic.items()]))

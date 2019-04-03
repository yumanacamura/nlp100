from  nlp027 import dic
import re
p = [[re.compile(i[0]),i[1]] for i in
[[r"\[[^\]]*?([^ \]]*)\]",r'\1'],[r"<.+?>",'']]]
for k,v in dic.items():
    dic[k] = p[1][0].subn(p[1][1],p[0][0].subn(p[0][1],v)[0])[0]
if __name__ == '__main__':
    print('\n'.join(['{0}:{1}'.format(k,v) for k,v in dic.items()]))

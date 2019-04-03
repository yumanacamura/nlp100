s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dic = {}
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for i,atom in enumerate(s.split()):
    dic[atom[0:1+(i+1 not in l)]] = i+1
print(dic)

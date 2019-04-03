s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
rm = [',','.']
for i in rm:
    s=s.replace(i,'')

l=[len(i) for i in s.split()]
print(l)

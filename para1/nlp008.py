def cipher(s):
    return ''.join([chr(219-ord(i)) if (ord(i)>96 and ord(i) < 123) else i for i in s ])

print(cipher('This is SECRET MESSAGE!'))

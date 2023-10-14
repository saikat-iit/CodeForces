s = input()
s = s[1:-1].split(sep=', ')
print(len(set(s)) if s[0] != "" else 0)
 
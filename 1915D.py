for _ in range(int(input())):
  n = int(input())
  s = list(input())
  v = ["a","e"]
  
  for i in range(2,len(s)):
    if s[i] in v:
      s[i-1] = "."+s[i-1]
  print(*s,sep='')
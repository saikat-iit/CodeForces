alphabets = []

for i in range(26):
    alphabets.append(chr(ord("a")+i))

for _ in range(int(input())):
    encrypted = []
    n = int(input())
    code = list(map(int, list(input())))
    while(n>0):
        i = n-1
        if code[i] != 0:
            encrypted.append(chr(ord("a")+code[i]-1))
            n = n - 1

        else:
            c = int(str(code[i-2])+str(code[i-1]))
            n = n - 3
            encrypted.append(chr(ord("a")-1+c))

    rEncrypt = ''
    for i in range(len(encrypted)-1, -1, -1):
        rEncrypt = rEncrypt + encrypted[i]

    print(rEncrypt)
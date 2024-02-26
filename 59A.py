word = input()

def caps(word:str):
    count = 0
    for i in list(word):
        if (ord(i) >= 97):
            count += 1
    
    if count >= len(word)-count:
        return False
    else: return True

if caps(word): print(word.upper())
else: print(word.lower())
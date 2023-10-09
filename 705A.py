n = int(input())
hate = "I hate that"
love = "I love that"

result = ''

for i in range(n):
    if i % 2 == 0:
        result = result + " " + hate
    else:
        result = result + " " + love

print(result[:-5].strip() + " it")
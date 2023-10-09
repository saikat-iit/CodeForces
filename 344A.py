n = int(input())
magnets = []
joined_magnets = []
joined = []
counter = 0

for i in range(n):
    magnet = int(input())
    magnets.append(magnet)

magnets.append(-1)

for i in range(len(magnets)-1):
    if magnets[i] == magnets[i+1]:
        joined_magnets.append(magnets[i])
        continue
    else:
        joined_magnets.append(magnets[i])
        joined.append(joined_magnets)
        joined_magnets = []

print(len(joined))
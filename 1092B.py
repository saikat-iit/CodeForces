n = int(input())
teams = list(map(int, input().split()))
teams.sort()

skills = 0
for i in range(0,len(teams)-1,2):
    skills += (teams[i+1] - teams[i])

print(skills)
ip = (input()).split()
n = int(ip[0])
k = int(ip[1])

counter = 0

if n >= k:
    if k >= 1 and k <= 50:
        score = (input()).split()
        K = int(score[k-1])
        if K != 0:
            for i in score:
                if int(i) >= K:
                    counter = counter + 1
        else:
            for i in score:
                if int(i) > K:
                    counter = counter + 1
 
print(counter)
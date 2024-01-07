n = input()
arr = list(map(int, input().split()))

def frequency(arr:list):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else: freq[item] = 1

    return freq

max_freq = max(frequency(arr).values())
print(len(arr) - max_freq)
    

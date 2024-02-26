import requests
methodName = "problemset.problems"
url= f"https://codeforces.com/api/{methodName}"

r = requests.get(url)
data = r.json()
data = data['result']['problems']
contestID = int(input("contest ID >>> "))
index = input("index >>> ")

d = next((item for item in data if(item["contestId"] == contestID) and item['index'] == index), False)
print(d)
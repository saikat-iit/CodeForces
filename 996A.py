n = int(input())
dollars = [100,20,10,5,1]
bills = 0

for dollar in dollars:
    bill = (n//dollar)
    bills = bills + bill
    n = n - dollar*bill

print(bills)
month = input()
n = int(input())
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_num = months.index(month) + 1
print(months[(n+month_num)%12-1])
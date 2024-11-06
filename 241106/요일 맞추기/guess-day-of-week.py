m1,d1,m2,d2 = map(int, input().split())
weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
month_date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def total_date(m, d):
    sum = 0
    for i in range(m):
        sum += month_date[i]
    return (sum + d)

diff = total_date(m2, d2) - total_date(m1, d1)
print(weekday[(1+diff)%7])
def month_sum(m):
    sum = 0
    for i in range(m):
        sum += month_date[i]
    return sum

month_date = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
m1, d1, m2, d2 = map(int, input().split())


print((month_sum(m2)+d2) - (month_sum(m1) + d1) + 1)
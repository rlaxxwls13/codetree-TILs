n = int(input())
count = 0

def beautiful_number(curr_num):
    global count
    if curr_num >= n + 1:
        if curr_num == n + 1:
            count += 1
        return
        
    for i in range(1, 5):
        if curr_num + i > n + 1:
            break
        beautiful_number(curr_num + i)
    return

beautiful_number(1)
print(count)
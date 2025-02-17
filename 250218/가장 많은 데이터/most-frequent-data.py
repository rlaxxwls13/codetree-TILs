n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

words_cnt = dict()
ans = 0

for word in words:
    if word in words_cnt:
        words_cnt[word] += 1
    else:
        words_cnt[word] =  1
    ans = max(words_cnt[word], ans)

print(ans)


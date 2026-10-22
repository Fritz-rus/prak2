n = int(input())
g = n // (17*29)
t = n % (17*29)
s = t // 29
k = t % 29
if g:
    print(g, "галлеонов")
if s:
    print(s, "сиклей")
if k:
    print(k, "кнатов")
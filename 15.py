n, k, m = map(int, input().split())
way1 = abs(k - m)
way2 = n - way1
result = 0
if way1 < way2:
    result = way1 - 1
else:
    result = way2 - 1

if result < 0:
    result = 0

print(result)
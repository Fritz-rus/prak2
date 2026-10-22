n, m = map(int, input().split("x"))
k = int(input())
K = []
t = 0

for i in range(1, n):
    K.append(i*m)
for i in range(1, m):
    K.append(i*n)

for i in K:
    if i == k:
        t+=1
        break

if t == 1:
    print("успешно")
else:
    print("неосуществимо")
a, b = map(int, input().split("x"))
c, d, f = map(int, input().split("x"))

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
if d > f:
    d, f = f, d
if c > d:
    c, d = d, c

if c <= a and d <= b:
    print("да")
else:
    print("нет")
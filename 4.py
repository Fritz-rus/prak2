t1, t2 = map(int, input().split(":"))
if t1 > t2:
    print(1)
elif t2 > t1:
    print(2)
elif t1 == t2:
    print(0)
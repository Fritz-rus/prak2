t1, t2, t3 = map(int, input().split())
if t1 >= t2 and t1 >= t3:
    print(t1)
elif t2 >= t1 and t2 >= t3:
    print(t2)
else:
    print(t3)
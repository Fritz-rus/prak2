n = int(input())
k = 0
p1, p2, p3, p4 = n // 1000, (n//100)%10, (n//10)%10, n%10
if 1000 <= n <= 9999:
    k+=1
if (p1 != p2 and p1 != p3 and p1 != p4) and (p2 != p1 and p2 != p3 and p2 != p4) and (p3 != p2 and p3 != p1 and p3 != p4) and (p4 != p2 and p4 != p3 and p4 != p1):
    k+=1
if 1900 <= n <= 2050:
    k = 0
else:
    k +=1

if k == 3:
    print("OK")
else:
    print("ERROR")
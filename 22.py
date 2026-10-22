from math import *

n, k, m = map(int, input().split())
s = 0
if k>=n:
    s = 2
else:
    s = ceil((2*n) / k)

print(s*m)
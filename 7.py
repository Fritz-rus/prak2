n = int(input())
if n // 1000 == n % 10 and (n//10)%10 == (n//100)%10:
    print("настоящее")
else:
    print("кривое")
n = int(input())

if n == 1:
    print(0)
else:
    n -= 1
    if n <=9:
        print(n)
    elif n <= 189:
        n -= 9
        p = 10 + (n-1)//2
        i = (n-1)%2
        if i == 0:
            print(p//10)
        else:
            print(p%10)
    else:
        n -= 189
        p = 100 + (n-1)//3
        i = (n-1)%3
        if i == 0:
            print(p//100)
        elif i == 1:
            print((p//10)%10)
        else:
            print(p%10)

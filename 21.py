m = input()
c1 = ord(m[0]) - 97 + 1
c2 = ord(m[3]) - 97 + 1
n1 = int(m[1])
n2 = int(m[4])

if (abs(c1 - c2) == 1 and abs(n1 - n2) == 2) or (abs(c1 - c2) == 2 and abs(n1 - n2) == 1):
    print("верно")
else:
    print("ошибка")
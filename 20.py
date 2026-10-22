m = input()
s = int(ord(m[0])) - 97 + 1
if (s + int(m[1])) % 2 == 0:
    print("черный")
else:
    print("белый")
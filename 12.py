c = int(input())
if c % 10 == 1 and c != 11:
    print(f'{c} попугай')
elif (c % 10 == 2 or c % 10 == 3 or c % 10 == 4) and (c != 12 or c != 13 or c != 14):
    print(f"{c} попугая")
else:
    print(f"{c} попугаев")
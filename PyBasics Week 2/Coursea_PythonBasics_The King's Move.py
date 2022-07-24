a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a - c) ** 2 > 1 or (b - d) ** 2 > 1:
    print("NO")
elif (a - c) == 0 and (b - d) == 0:
    print('NO')
else:
    print("YES")

# Найти макс.число из 3 введеных не используя max
x = int(input())
y = int(input())
z = int(input())
if x > y > z:
    print(x)
elif x < y < z:
    print(z)
else:
    print(y)

# Если число симметрично(2002) то выводит 1 если нет 0
n = int(input())
n3 = (n // 10 ** 1) % 10
n2 = (n // 10 ** 2) % 10
n1 = (n // 10 ** 3) % 10
n4 = (n % 10 ** 1)
if n1 == n4 and n2 == n3:
    print(1)
else:
    print(0)

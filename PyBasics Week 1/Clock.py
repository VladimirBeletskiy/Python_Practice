#С начала суто прошло N минут. Вывести текущее время
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

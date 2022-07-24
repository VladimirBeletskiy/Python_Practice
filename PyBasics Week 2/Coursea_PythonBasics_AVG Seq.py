# Найти среднее значение последовательности
#Когда закончишь последовательность кончается пишим 0
sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)

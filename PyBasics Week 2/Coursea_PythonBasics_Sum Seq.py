#Определите сумму всех элементов последовательности, завершающейся числом 0.
sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)

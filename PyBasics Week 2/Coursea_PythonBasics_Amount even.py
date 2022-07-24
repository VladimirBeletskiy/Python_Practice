# Посчитать кол_во ченых элементов последовательности
# Когда последовательность кончилась пиши 0
num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)

#Даны значения двух моментов времени, принадлежащих одним и тем же суткам:
#часы, минуты и секунды для каждого из моментов времени.
#Известно, что второй момент времени наступил не раньше первого.
#Определите, сколько секунд прошло между двумя моментами времени.
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
print((x - a) * 3600 + (y - b) * 60 + z - c)

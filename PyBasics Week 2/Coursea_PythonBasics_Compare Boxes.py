#Есть две коробки, первая размером A₁×B₁×C₁,
#вторая размером A₂×B₂×C₂.Определите, можно ли
#разместить одну внутри другой, при условии,
#что поворачивать коробки можно только на 90 градусов вокруг ребер.
a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
b1 = int(input())
c1 = int(input()) 
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a1 > c1:
    a1, c1 = c1, a1
if b1 > c1:
    b1, c1 = c1, b1
if a1 > b1:
    a1, b1 = b1, a1
if a == a1 and b == b1 and c == c1:
    print('Boxes are equal')
elif a <= a1 and b <= b1 and c <= c1:
    print('The first box is smaller than the second one')
elif a >= a1 and b >= b1 and c >= c1:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')

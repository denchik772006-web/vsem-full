#Вычисление целых корней уравнения по системе Горнера, python
n = int(input('Запишите максимальную степень: ')) + 1
k = list(map(int, input('Запишите коэффициенты уравнения: ').split()))

roots = []
coeffs = k[:]

while len(coeffs) > 1 and coeffs[-1] == 0:
    roots.append(0)
    coeffs.pop()

if len(coeffs) > 1:
    a0 = abs(coeffs[-1])
    divs = []
    for d in range(1, a0 + 1):
        if a0 % d == 0:
            divs.append(d)
            divs.append(-d)

    for r in divs:
        while True:
            b = [coeffs[0]]
            for j in range(1, len(coeffs)):
                b.append(b[-1] * r + coeffs[j])
            if b[-1] == 0:
                roots.append(r)
                coeffs = b[:-1]
                if len(coeffs) == 1:
                    break
            else:
                break
print("Корни:", *roots, sep=' ')
print("Оставшиеся коэффициенты:", *coeffs)

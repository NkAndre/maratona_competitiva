linha1 = input().split()
a = float(linha1[0])
b = float(linha1[1])
c = float(linha1[2])

if a < b + c and b < a + c and c < a + b:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = (a + b) * c / 2
    print(f'Area = {area:.1f}')
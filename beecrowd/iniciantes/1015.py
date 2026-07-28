linha1 = input().split()
a = float(linha1[0])
b = float(linha1[1])

linha2 = input().split()
c = float(linha2 [0])
d = float(linha2 [1])

distancia = ((c  - a )**2 + (d - b)**2) **0.5
print(f'{distancia:.4f}')
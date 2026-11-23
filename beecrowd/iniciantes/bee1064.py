soma = 0
positivos = 0

for i in range(6):
    numero = float(input())
    if numero > 0:
        positivos += 1
        soma += numero

if positivos > 0:
    media = soma / positivos
    print(f"{positivos} valores positivos")
    print(f"{media:.1f}")

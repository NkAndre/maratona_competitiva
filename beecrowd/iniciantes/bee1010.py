linha1 = input().split()
cod_peca1 = int(linha1[0])
numero_pecas1 = int(linha1[1])
valor_unitario1 = float(linha1[2])

linha2 = input().split()
cod_peca2 = int(linha2[0])
numero_pecas2 = int(linha2[1])
valor_unitario2 = float(linha2[2])

valor_pago = (numero_pecas1 * valor_unitario1) + (numero_pecas2 * valor_unitario2)

print(f'VALOR A PAGAR: R$ {valor_pago:.2f}')

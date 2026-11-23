nome  = (input())
salario_fixo = float(input())
total_vendas = float(input())

total = total_vendas  *0.15
total_receber = salario_fixo + total

print(f'TOTAL = R$ {total_receber:.2f}')

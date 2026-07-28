numero = int(input())
horas_total = numero // 3600
resto_segundos  =numero % 3600
minutos = resto_segundos // 60
segundos_finais=  resto_segundos%60
print(f'{horas_total}:{minutos}:{segundos_finais}')

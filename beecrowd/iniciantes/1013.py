linha1 = input().split()

a = int(linha1[0])
b = int(linha1[1])
c = int(linha1[2])

maiorAb = (a+b +abs (a-b)) //2
maiorFinal = (maiorAb+c +abs (maiorAb-c)) //2
print(f'{maiorFinal} eh o maior')

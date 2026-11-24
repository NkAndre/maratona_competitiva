horaInicial, horaFinal = map(int, input().split())

if horaInicial < horaFinal:
    duracao = horaFinal - horaInicial
else:
    duracao = (24 - horaInicial) +horaFinal


print(f"O JOGO DUROU {duracao} HORA(S)")
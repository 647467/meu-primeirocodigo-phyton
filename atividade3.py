pontuacao = int(input("Digite a pontuação do jogador:"))

if pontuacao >= 1000:
    print("Nível alcançado: Mestre")
elif pontuacao >= 500:
    print("Nivel alcançado: Platina")
elif pontuacao >= 100:
    print("Nivel alcançado: Bronze")
else:
    print("continue jogando!")
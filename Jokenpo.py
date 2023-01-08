import random

usuario_vitoria = 0
AI_vitoria = 0
empate = 0

opcoes = ["pedra", "papel", "tesoura"]

while True:
    usuario_entrada = input("Escreva pedra, papel ou tesoura. Caso queira sair digite Q: ").lower()
    if usuario_entrada == "q":
        break

    if usuario_entrada not in opcoes:
        continue

    valor_aleatorio = random.randint(0, 2)
    # pedra: 0, papel: 1, tesoura: 2
    AI_escolha = opcoes[valor_aleatorio]
    print("Computador escolheu", AI_escolha + ".")

    if usuario_entrada == "pedra" and AI_escolha == "tesoura":
        print("Você venceu")
        usuario_vitoria += 1

    elif usuario_entrada == "papel" and AI_escolha == "pedra":
        print("Você venceu")
        usuario_vitoria += 1

    elif usuario_entrada == "tesoura" and AI_escolha == "papel":
        print("Você venceu")
        usuario_vitoria += 1

    elif usuario_entrada == "tesoura" and AI_escolha == "tesoura":
        print("Empate!")
        empate += 1

    elif usuario_entrada == "pedra" and AI_escolha == "pedra":
        print("Empate!")
        empate += 1

    elif usuario_entrada == "papel" and AI_escolha == "papel":
        print("Empate!")
        empate += 1

    else:
        print("Você perdeu!")
        AI_vitoria += 1

print("Você venceu", usuario_vitoria, "vezes.")
print("O computador venceu", AI_vitoria, "vezes.")
print("Empates aconteceram", empate, "vezes.")
print("Adeus!")
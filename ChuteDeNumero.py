import random

numero_maximo = input("Digite o número máximo: ")

if numero_maximo.isdigit():
    numero_maximo = int(numero_maximo)

    if numero_maximo <= 0:
        print('Por favor digite um número maior que 0 na próxima vez.')
        quit()
else:
    print('Por favor digite um número da próxima vez.')
    quit()

numero_aleatorio = random.randint(0, numero_maximo)
chutes = 0

while True:
    chutes += 1
    usuario_chute = input("Chute um número: ")
    if usuario_chute.isdigit():
        usuario_chute = int(usuario_chute)
    else:
        print('Por favor digite um número da próxima vez.')
        continue

    if usuario_chute == numero_aleatorio:
        print("Você acertou!")
        break
    elif usuario_chute > numero_aleatorio:
        print("Você chutou acima do número!")
    else:
        print("Você chutou abaixo do número!")
    if (chutes>1):
        print("Você acertou em", chutes, "chutes")
    else:
        print("Que sorte! Você acertou em 1 único chute!")

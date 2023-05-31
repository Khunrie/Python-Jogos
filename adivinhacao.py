import random

def jogar():

    print("*********************************")
    print("Bem Vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute = int(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou {chute}")

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        menor   = chute < numero_secreto
        maior   = chute > numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (menor):
                print("Você errou! Seu chute foi menor que o número secreto.")
            elif (maior): 
                print("você errou! Seu chute foi maior que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("--------------------------")

    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()
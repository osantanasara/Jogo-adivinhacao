import random

def jogar():
    print("Bem-vindo ao Jogo de Adivinhação!")

    numero_secreto = random.randint(1, 100)
    total_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for tentativa_atual in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa_atual, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("O número deve estar entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            print("Parabéns, você ganhou!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    if not acertou:
        print("O número secreto era {}. Você perdeu!".format(numero_secreto))
        print("Fim do jogo!")


if __name__ == '__main__':
    jogar()

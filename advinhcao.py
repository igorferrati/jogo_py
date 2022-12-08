import random

def jogar_advinhacao():

    msg_inicio()
    num_secreto = random.randint(1,100)
    nivel = escolhe_nivel()
    tentativas = nivel_game(nivel)
    rodada = 1
    score = 1000

    while rodada <= tentativas:

        print(f'{"......................Advinhe o número......................":^50}')
        print(f'[rodada:{rodada}/{tentativas}]')
        num_chute = int(input(f'Qual número estou pensando [1 - 100]?: '))

        if num_chute < 1 or num_chute > 100:
            print('Ooops número invalido!! Digite um número entre 1 e 100')
            continue

        certo = num_secreto == num_chute
        maior = num_chute > num_secreto
        menor = num_chute < num_secreto

        if certo:
            print('Você acertou !!!!!')
            break
        else:
            if maior:
                print('Você errou! Tente um número menor')
                print(20*'---')
            elif menor:
                print('Você errou! Tente um número maior')
                print(20*'---')

            score_erro = abs(num_secreto - num_chute)
            score = score - score_erro
        rodada += 1

    print(20*'---')
    print(f'O número secreto é: {num_secreto}')
    print(f'Você fez {score} pontos')
    print(20*'---')
    print('Fim de jogo !!')


#Funções

def msg_inicio():
    print(30*'**')
    print(f'{"Bem vindo ao jogo de Advinhação":^60}')
    print(30*'**')


def escolhe_nivel():
    print('Escolha um nível de dificuldade')
    print('[1]- Fácil   [2]- Médio   [3]- Difícil')
    nivel = int(input(': '))
    return nivel


def nivel_game(nivel):
    tentativas = 0
    if nivel == 1:
        tentativas = 20
        print(f'Você possuí {tentativas} tentativas, boa sorte !')
        return tentativas
    elif nivel == 2:
        tentativas = 10
        print(f'Você possuí {tentativas} tentativas, boa sorte !')
        return tentativas
    else:
        tentativas = 5
        print(f'Você possuí {tentativas} tentativas, boa sorte !')
        return tentativas

if __name__ == '__main__':
    jogar_advinhacao()


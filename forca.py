import random

def jogar_forca():
    print_abertura()
    palavra_secreta = cria_palavra()
    letras_acerto = inicia_letras(palavra_secreta)
    print(f'Palavra: {letras_acerto}')

    perdeu = False
    acertou = False
    erros = 0

    while not perdeu and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            letras_certas(chute, letras_acerto, palavra_secreta)
        else:
            erros += 1
            
        perdeu = erros == 6
        acertou = '_' not in letras_acerto
        print(letras_acerto)

    if acertou:
        msg_ganhar(palavra_secreta)
    else:
        msg_perder(palavra_secreta)

    print(20*'---')
    print('Fim de jogo !!')

#Funções
def print_abertura():
    print(20*'***')
    print('----------------------- JOGO DA FORCA ----------------------')
    print(20*'***')


def cria_palavra():
    arquivo = open('arquivo.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # tratando /n do txt
        palavras.append(linha)

    arquivo.close()

    n = random.randrange(0, len(palavras))
    escolhe_palavra = palavras[n].upper()
    return escolhe_palavra


def inicia_letras(palavra):
    return ['_' for letra in palavra]


def pede_chute():
    chute = input('Escolha uma letra: ')
    chute = chute.strip().upper()
    return chute


def letras_certas(chute, letras_acerto, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acerto[index] = letra
        index += 1


def msg_ganhar(palavra_secreta):
    print(f'Parabéns !! Você Acertou!\n Palavra: {palavra_secreta}')


def msg_perder(palavra_secreta):
    print('Oh não, você perdeu')
    print(f'A palavra é {palavra_secreta} !')


if __name__ == '__main__':
    jogar_forca()

import forca
import advinhcao


print(20 * '***')
print(f'{"************** Escolha o Jogo **************":^60}')
print(20 * '***')

print('[1] Jogo da Forca\n'
      '[2] Jogo da Advinhação')
jogo = 0

while jogo != 1 or 2:
    jogo = input('Qual jogo?: ')
    if jogo.isnumeric():
        jogo = int(jogo)
        if jogo == 1:
            print(20 * '---')
            print('Jogando Forca')
            forca.jogar_forca()
            break
        elif jogo == 2:
            print(20 * '---')
            print('Jogando Advinhação')
            advinhcao.jogar_advinhacao()
            break
        elif jogo != 1 or 2:
            print('Escolha entre [1] Jogo da Forca ou [2] Jogo da Advinhação')
    else:
        print('Escolha entre [1] Jogo da Forca ou [2] Jogo da Advinhação')

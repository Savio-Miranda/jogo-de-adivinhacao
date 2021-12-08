from adivinhacao import jogo_de_adivinhacao
from forca import jogo_da_forca


menu = True
while menu:
    jogos = input('Que jogo você quer jogar?\n'
                  '[1] Adivinhação, [2] Forca ou qualquer botão para encerrar o menu.\n'
                  '-> ')

    if jogos == '1':
        jogo_de_adivinhacao.executar()
        continue

    elif jogos == '2':
        jogo_da_forca.executar()
        continue

    else:
        print('Menu encerrado.')
        break

from adivinhacao import jogo_de_adivinhacao
from forca import jogo_da_forca

jogos = input('Que jogo você quer jogar?\n'
              '[1] Adivinhação, [2] Forca\n'
              '-> ')
menu = True
while menu:
    if jogos == '1':
        jogo_de_adivinhacao.executar()
        continue

    elif jogos == '2':
        jogo_da_forca.executar()
        continue

    else:
        break

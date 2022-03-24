from adivinhacao import regras_da_advinhacao


def executar():
    print(36 * '*')
    print('Bem-vindo(a) ao jogo de adivinhação!')
    print(36 * '*', end='\n\n')
    print('A pontuação máxima para cada dificuldade é:\n'
          '20 em Fácil, 40 em Médio e 60 em Difícil.\n')

    dificuldade_das_regras = {'1': lambda: regras_da_advinhacao.jogo((6, 10, 20)),
                              '2': lambda: regras_da_advinhacao.jogo((5, 20, 40)),
                              '3': lambda: regras_da_advinhacao.jogo((4, 30, 60))}

    jogar = True
    while jogar:
        dificuldade = input('Escolha a dificuldade pressionando as seguintes teclas:\n'
                            '[1] Fácil, [2] Médio, [3] Difícil ou entre com qualquer tecla para VOLTAR AO MENU\n'
                            '-> ')

        if dificuldade not in dificuldade_das_regras:
            print('Você saiu do jogo!\n')
            break

        dificuldade_das_regras[dificuldade]()


if __name__ == '__main__':
    executar()

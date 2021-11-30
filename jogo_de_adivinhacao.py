import regras

print(36 * '*')
print('Bem-vindo(a) ao jogo de adivinhação!')
print(36 * '*', end='\n\n')

DIFICULDADE_DAS_REGRAS = {'1': lambda: regras.jogo((6, 7)),
                          '2': lambda: regras.jogo((5, 20)),
                          '3': lambda: regras.jogo((4, 30))}

jogar = True
while jogar:
    dificuldade = input('Escolha a dificuldade pressionando as seguintes teclas:\n'
                        '[1] Fácil, [2] Médio, [3], Difícil, ou qualquer tecla para SAIR\n'
                        '-> ')

    if dificuldade not in DIFICULDADE_DAS_REGRAS:
        print('Você saiu do jogo!')
        break

    DIFICULDADE_DAS_REGRAS[dificuldade]()

print('Fim de jogo')

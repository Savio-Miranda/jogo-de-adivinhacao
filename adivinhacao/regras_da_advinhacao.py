import random


def jogo(nivel):  # O nível do jogo é baseado no número de rodadas e no limite do jogo (de 1 até n).
    numero_de_rodadas, limite_do_jogo, pontuacao_final = nivel

    numero_secreto = random.randrange(1, limite_do_jogo + 1)
    print('Digite um número de 1 até {}!'.format(limite_do_jogo))

    for rodada in range(1, numero_de_rodadas):
        print('Rodada: {} de {}!'.format(rodada, numero_de_rodadas - 1))
        chute = int(input('-> '))

        if (1 > chute) or (limite_do_jogo < chute):
            print('Entrada inválida. Por favor, atenha-se às regras.')
            continue

        if chute == numero_secreto:
            print('Você conseguiu! O número secreto era {}!'.format(numero_secreto))
            return print("Pontuação:", pontuacao_final)

        else:
            if rodada == numero_de_rodadas - 1:
                print('Você perdeu! O número secreto era:', numero_secreto)
                break

            if chute > numero_secreto:
                print('Errou! O número digitado é MAIOR do que o número secreto!')

            else:
                print('Errou! O número digitado é MENOR do que o número secreto!')

            pontuacao_final -= abs(chute - numero_secreto)

    pontuacao_final = 0
    return print('Pontuação final: {}'.format(pontuacao_final))

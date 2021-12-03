def substituidor_de_letras(index, letra, palavra):
    criar_lista = list(palavra)
    criar_lista[index] = letra
    return criar_lista


def executar():
    print(36 * '*')
    print('Bem-vindo(a) ao jogo da forca!')
    print(36 * '*', end='\n\n')

    palavra_secreta = input('Peça a um amigo digitar a palavra secreta!\n-> ').upper().strip()
    chances = 5

    letras_corretas = ''
    letras_usadas = []

    for contador_de_palavra in range(len(palavra_secreta)):
        letras_corretas += '_ '
    print('Palavra secreta:', letras_corretas)

    letras_corretas = letras_corretas.replace(' ', '')

    while chances > 0:
        index_da_letra = 0

        chute = input('Digite uma letra: ').upper().strip()
        if len(chute) > 1:
            print('Entrada inválida! Atente-se às regras.')
            continue

        elif chute in letras_usadas:
            chances -= 1
            print('Você já digitou essa entrada. Agora você possui {} chance(s).'.format(chances))

        elif chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_corretas = substituidor_de_letras(index_da_letra, letra, letras_corretas)
                    if letra not in letras_usadas:
                        letras_usadas.append(letra)

                index_da_letra += 1

        else:
            chances -= 1
            print('Você errou e possui agora {} chance(s).'.format(chances))
            letras_usadas.append(letras_usadas)
            if chances == 0:
                print('Você perdeu!')

        print('letras usadas:', letras_usadas, '\n')

        palavra_completa = ''.join(letras_corretas)

        palavra_completa_e_lacunada = ' '.join(letras_corretas)

        print('Palavra secreta:', palavra_completa_e_lacunada)

        if palavra_completa == palavra_secreta:
            print('Você venceu!')
            break


if __name__ == '__main__':
    while True:
        executar()
        finalizar = input('Finalizar? [S] para finalizar, qualquer tecla para continuar: ').upper()
        if finalizar == 'S':
            break

    print('fim de jogo')

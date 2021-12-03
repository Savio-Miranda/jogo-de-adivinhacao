def substituidor_de_letras(index, letra, palavra):
    criador_de_lista_a_partir_de_palavras = list(palavra)
    criador_de_lista_a_partir_de_palavras[index] = letra

    palavra = "".join(criador_de_lista_a_partir_de_palavras)

    return palavra


def executar():
    print(36 * '*')
    print('Bem-vindo(a) ao jogo da forca!')
    print(36 * '*', end='\n\n')

    palavra_secreta = input('Peça a um amigo digitar a palavra secreta!\n-> ').upper().strip()
    chance = 5

    lacuna = ''
    for contador_de_palavra in range(len(palavra_secreta)):
        lacuna += '_'
    print('Palavra secreta: ', lacuna)

    while (not lacuna == palavra_secreta) and (chance > 0):
        index_da_letra = 0

        chute = input('Digite uma letra: ').upper().strip()
        if len(chute) > 1:
            print('Entrada inválida! Atente-se às regras.')
            continue

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    lacuna = substituidor_de_letras(index_da_letra, letra, lacuna)

                if lacuna == palavra_secreta:
                    print('Você venceu!')
                    break

                index_da_letra += 1

        else:
            chance -= 1
            print('Você errou e possui agora {} chance(s).'.format(chance))
            if chance == 0:
                print('Você perdeu!')
        print('Palavra secreta: ', lacuna)


if __name__ == '__main__':
    while True:
        executar()
        finalizar = input('Finalizar? [S] para finalizar, qualquer tecla para continuar: ')
        if finalizar == 'S':
            break

    print('fim de jogo')

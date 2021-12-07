from forca import regras_da_forca


def executar():
    regras_da_forca.impressor_de_boas_vindas()

    palavra_secreta = input('Peça a um amigo digitar a palavra secreta!\n-> ').upper().strip()
    palavra_secreta = regras_da_forca.tratamento_da_palavra(palavra_secreta)

    chances = 5
    letras_usadas = []
    lacunas = regras_da_forca.criar_lacunas(palavra_secreta)
    print('Palavra secreta:', lacunas)

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
                if letra == ' ':
                    index_da_letra += 1
                    continue
                elif letra == chute:
                    lacunas = regras_da_forca.substituidor_de_letras(index_da_letra, letra, lacunas)

                    if chute not in letras_usadas:
                        letras_usadas.append(letra)

                index_da_letra += 1

        else:
            chances -= 1
            print('Você errou e possui agora {} chance(s).'.format(chances))
            letras_usadas.append(letras_usadas)

        palavra_preenchida = ''.join(lacunas)
        print('Palavra secreta:', palavra_preenchida)

        if chances == 0:
            print('Você perdeu!')
            break

        if palavra_preenchida == palavra_secreta:
            print('Você venceu!')
            break


if __name__ == '__main__':
    while True:
        executar()
        finalizar = input('Finalizar? [S] para finalizar, qualquer tecla para continuar: ').upper()
        if finalizar == 'S':
            break

    print('fim de jogo')

def impressor_de_boas_vindas(chances):
    print(36 * '*')
    print('   Bem-vindo(a) ao jogo da forca!')
    print(36 * '*', end='\n')
    print('       Você tem {} chances!'.format(chances))


def tratamento_da_palavra(palavra_secreta):
    palavra_secreta = list(palavra_secreta)
    palavra_tratada = ' '.join(palavra_secreta)

    return palavra_tratada


def criar_lacunas(palavra_tratada):
    lacunas = ''
    for contador_de_caracteres in palavra_tratada:
        if contador_de_caracteres == ' ':
            lacunas += ' '
            continue
        lacunas += '_'

    return lacunas


def substituidor_de_letras(index, letra, palavra_secreta):
    criar_lista = list(palavra_secreta)
    criar_lista[index] = letra

    return criar_lista


def entrada_repetida(chute, letras_usadas, chances):
    if (len(chute) == 1) and (chute in letras_usadas):
        chances -= 1
        return 'Entrada repetida! Agora você possui {} chances.'.format(chances)


def entrada_incorreta(chute, palavra_secreta, chances, letras_usadas):
    if chute not in palavra_secreta:
        chances -= 1
        letras_usadas.append(chute)
        return 'Você errou e possui agora {} chance(s).'.format(chances)


def entrada_correta(chute, palavra_secreta, index, lacunas, letras_usadas):
    if chute in palavra_secreta:
        for letra in palavra_secreta:
            if letra == ' ':
                index += 1
                continue
            elif letra == chute:
                lacunas = substituidor_de_letras(index, letra, lacunas)

                if chute not in letras_usadas:
                    letras_usadas.append(letra)

            index += 1
        return lacunas


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def impressor_de_boas_vindas(chances):
    print(36 * '*')
    print('   Bem-vindo(a) ao jogo da forca!')
    print(36 * '*', end='\n')
    print('       Você tem {} chances!'.format(chances))


def tratamento_da_palavra(palavra):
    palavra = list(palavra)
    palavra_tratada = ' '.join(palavra)

    return palavra_tratada


def criar_lacunas(palavra_tratada):
    lacunas = ''
    for contador_de_caracteres in palavra_tratada:
        if contador_de_caracteres == ' ':
            lacunas += ' '
            continue
        lacunas += '_'

    return lacunas


def substituidor_de_letras(index, letra, palavra):
    criar_lista = list(palavra)
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

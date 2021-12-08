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


def executar():
    letras_usadas = []
    chances = 5
    index_da_letra = 0

    impressor_de_boas_vindas(chances)

    palavra_secreta = input('Peça a um amigo digitar a palavra secreta!\n-> ').upper().strip()
    palavra_secreta = tratamento_da_palavra(palavra_secreta)

    lacunas = criar_lacunas(palavra_secreta)
    print('Palavra secreta:', lacunas)

    while chances > 0:

        chute = input('Digite uma letra: ').upper().strip()
        if len(chute) > 1:
            print('Entrada inválida! Você adicionou mais de um caractere. Tente de novo.')
            continue

        possibilidades_da_forca = {
            '1': entrada_repetida(chute, letras_usadas, chances),
            '2': entrada_incorreta(chute, palavra_secreta, chances, letras_usadas),
            '3': entrada_correta(chute, palavra_secreta, index_da_letra, lacunas, letras_usadas)
        }

        for selecao in possibilidades_da_forca:
            saida = possibilidades_da_forca[selecao]

            if type(saida) == str:
                chances -= 1
                if chances == 0:
                    print('Você perdeu!')
                    break
                print(saida)
                break

            elif type(saida) == list:
                lacunas = saida
                palavra_preenchida = ''.join(lacunas)
                print('Palavra secreta:', palavra_preenchida)
                if palavra_preenchida == palavra_secreta:
                    print('Você venceu!')
                    chances = 0
                    break

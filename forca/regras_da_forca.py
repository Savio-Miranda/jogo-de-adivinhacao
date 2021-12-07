def impressor_de_boas_vindas():
    print(36 * '*')
    print('Bem-vindo(a) ao jogo da forca!')
    print(36 * '*', end='\n')


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

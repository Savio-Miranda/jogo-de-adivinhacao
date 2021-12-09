from forca import regras_da_forca


def executar():
    letras_usadas = []
    chances = 5
    index_da_letra = 0

    regras_da_forca.impressor_de_boas_vindas(chances)

    palavra_secreta = input('Peça a um amigo digitar a palavra secreta! Mas se quiser voltar ao MENU, '
                            'pressione ENTER.\n-> ').upper().strip()
    palavra_secreta = regras_da_forca.tratamento_da_palavra(palavra_secreta)

    lacunas = regras_da_forca.criar_lacunas(palavra_secreta)
    if lacunas == '':
        print('Você saiu do jogo!\n')
    else:
        print('Palavra secreta:', lacunas)

    while chances > 0:
        if palavra_secreta == '':
            break

        chute = input('Digite uma letra: ').upper().strip()
        if len(chute) > 1:
            print('Entrada inválida! Você adicionou mais de um caractere. Tente de novo.')
            continue

        possibilidades_da_forca = {
            '1': regras_da_forca.entrada_repetida(chute, letras_usadas, chances),
            '2': regras_da_forca.entrada_incorreta(chute, palavra_secreta, chances, letras_usadas),
            '3': regras_da_forca.entrada_correta(chute, palavra_secreta, index_da_letra, lacunas, letras_usadas)
        }

        for selecao in possibilidades_da_forca:
            saida = possibilidades_da_forca[selecao]

            if type(saida) == str:
                chances -= 1
                if chances == 0:
                    regras_da_forca.imprime_mensagem_perdedor(palavra_secreta)
                    break
                print(saida)
                break

            elif type(saida) == list:
                lacunas = saida
                palavra_preenchida = ''.join(lacunas)
                print('Palavra secreta:', palavra_preenchida)
                if palavra_preenchida == palavra_secreta:
                    regras_da_forca.imprime_mensagem_vencedor()
                    chances = 0
                    break


if __name__ == '__main__':
    executar()

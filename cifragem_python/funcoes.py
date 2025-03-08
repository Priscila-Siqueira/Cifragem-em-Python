def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: # with fechar o arquivo após ele ser aberto após ele ser usado
      return arquivo.read().strip() # 'r' = abri um arquivo   read() = lê um arquivo    strip() = tira espaços das strings


def exportar_arquivo(texto_arquivo, nome_do_metodo_cifragem):
    print(texto_arquivo)
    novo_nome_arquivo = f"arquivo_original_{nome_do_metodo_cifragem}.txt"
    # Grava o texto no novo arquivo
    with open(novo_nome_arquivo, 'w', encoding='utf-8') as novo_arquivo:
        novo_arquivo.write(texto_arquivo)

    print(f"\nArquivo '{novo_nome_arquivo}' criado com sucesso!")


def inverter_mensagem(texto):
    return texto[::-1]


def deslocamento_de_letras(texto_arquivo, numero_deslocamento):

   #            0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
   alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   resultado = ""

   for letra_do_texto in texto_arquivo:
        #  Converte a letra atual para maiúscula, para procurar no alfabeto
      letra_maiuscula = letra_do_texto.upper()

      #  Verifica se (a versão maiúscula) está no alfabeto
      if letra_maiuscula in alfabeto:
         #  Localiza a posição no alfabeto com o while (mantido do seu código)
         posicao = 0
         while posicao < len(alfabeto):
             if alfabeto[posicao] == letra_maiuscula:
                 break
             posicao += 1
         
         # Aplica o deslocamento circular
         nova_posicao_da_nova_letra = (posicao + numero_deslocamento) % len(alfabeto)
         
         # Pega a letra deslocada (em maiúscula)
         letra_deslocada_maiuscula = alfabeto[nova_posicao_da_nova_letra]
         
         # Se a letra original era minúscula, converte a deslocada para minúscula
         if letra_do_texto.islower():
             resultado += letra_deslocada_maiuscula.lower()
         else:
             # Se era maiúscula, mantém maiúscula
             resultado += letra_deslocada_maiuscula
      else:
          resultado += letra_do_texto

   return resultado


def substituicao_aleatoria_letras(texto_arquivo):
    matriz_para_subs_letras = [
        ['A', 'P'],
        ['B', '1'],
        ['C', '#'],
        ['D', 'X'],
        ['E', '*'],
        ['F', '8'],
        ['G', 'W'],
        ['H', '&'],
        ['I', '10'],
        ['J', 'Q'],
        ['K', '@'],
        ['L', '5'],
        ['M', '%'],
        ['N', 'Ç'],
        ['O', '4'],
        ['P', '/'],
        ['Q', 'S'],
        ['R', '9'],
        ['S', 'A'],
        ['T', 'F'],
        ['U', '?'],
        ['V', '3'],
        ['W', 'B'],
        ['X', '+'],
        ['Y', 'L'],
        ['Z', '6']
    ]

    resultado = ""

    for letra in texto_arquivo:
        maiuscula = letra.isupper()
        letra_maiuscula = letra.upper()

        substituto_encontrado = None

        for linha_matriz in matriz_para_subs_letras:
            letra_original = linha_matriz[0]
            valor_substituto = linha_matriz[1]

            if letra_maiuscula == letra_original:
                substituto_encontrado = valor_substituto
                break

        if substituto_encontrado is not None:
            if maiuscula:
                resultado += substituto_encontrado.upper()

            else:
                resultado += substituto_encontrado.lower()

        else:
            resultado += letra

    return resultado 










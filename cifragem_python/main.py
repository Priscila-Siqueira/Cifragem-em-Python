from funcoes import carregar_arquivo, exportar_arquivo,inverter_mensagem,deslocamento_de_letras,substituicao_aleatoria_letras


def main():
   nome_arquivo = input("Digite o nome do arquivo .txt: ")
   texto_arquivo = carregar_arquivo(nome_arquivo)

   print("=====================\n      MENU      \n=====================")
   print("1 - Inversão da mensagem")
   print("2 - Deslocamento de letras")
   print("3 - Substituição aleatória\n")

   opcao_escolhida = input("Selecione a opção com o tipo de método de cifragem que deseja: ")
  
   if opcao_escolhida == '1':
      texto_invertido = inverter_mensagem(texto_arquivo)
      exportar_arquivo(texto_invertido, "inversao_da_mensagem")

   elif opcao_escolhida == '2':
      numero_deslocamento = int(input("Digite o número de deslocamento (0 a 27): "));
      texto_deslocado = deslocamento_de_letras(texto_arquivo, numero_deslocamento);
      exportar_arquivo(texto_deslocado, "deslocamento_das_letras")

   elif opcao_escolhida == '3':
      texto_aleatorio = substituicao_aleatoria_letras(texto_arquivo);
      exportar_arquivo(texto_aleatorio, "substituição_aleatoria");
   
   else:
     print("OPÇÃO INVÁLIDA!") 

if __name__ == "__main__":
   main()
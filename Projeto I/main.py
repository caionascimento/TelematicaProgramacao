'''
Tabela de cores---------
exemplo: 
print '\033[31m'+'Isto eh vermelho'+'\033[0;0m'
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
------------------------
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
------------------------
branco = '\033[37m'
------------------------
restaura cor original = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'
-------------------------
fundo preto = '\033[40m'
fundo vermelho = '\033[41m'
fundo verde = '\033[42m'
fundo amarelo = '\033[43m'
fundo azul = '\033[44m'
fundo magenta = '\033[45m'
fundo ciano = '\033[46m'
fundo branco = '\033[47m'
-------------------------
'''
#Variaveis globais, não alterar
print ( "\n"  * 80 )
n=0
saida = "s"
opcao = "inicio"
letrasDigitadas = []
#listas das palavras da forca e suas dicas
listPalavras = ['WHILE', 'MKDIR', 'SUDO']
listDicas = ['Comando usado para repetição em linguagens de programação', 'Comando usado em Terminal Linux para criar um novo diretório', 'Comando usado em Terminal Linux para Verificar Permissões']
#Menu Inicial do Jogo
while (opcao != "quit"):
  print('''
Bem vindo a Plataforma Multijogos!!!

Digite (forca) para iniciar o Jogo da Forca
Digite (perguntas) para iniciar o Jogo de Perguntas e Respostas
Digite (quit) para encerrar a Plataforma Multijogos
Digite a senha para configurar a Plataforma Multijogos
  ''')
  opcao = input('\033[47m'+'\033[30m'+'\033[1m'+" Opção "+"\033[0;0m"+"\033[0;0m"+"\033[0;0m")
  #Opção do menu para casdatrar novas palavras (senha: admin123)
  if (opcao == 'admin123'):
    print ( "\n"  * 80 )
    print(" - Cadastro de palavras - ")
    print()
    #Solicita a PALAVRA e a DICA para cadastro
    while (saida == 's' or saida == 'S'):
      novaPalavra = str(input("Informe uma nova palavra:"))
      novaDica = str(input("Informe a dica da palavra:"))
      #Confirmação se a palavra e dica estão corretas para cadastro
      print('''
Se você realmente deseja cadastrar as informações a baixo, digite (ok)
Palavra: {}
Dica: {}
  '''.format(novaPalavra, novaDica))
      cadastro = input("\033[47m"+"\033[30m"+"\033[1m"+" Opção "+"\033[0;0m"+"\033[0;0m"+"\033[0;0m")
      #Teste se realmente o usuario vai cadastrar a PALAVRA e a DICA passada
      if (cadastro == "ok" or cadastro == "OK"):
        listPalavras.append(novaPalavra.upper())
        listDicas.append(novaDica)
        print("Palavra e Dica cadastradas com sucesso!\n")
      else: 
        print("Palavra e Dica não cadastradas")
      #Pergunta se deseja cadastrar mais palavras na lista
      saida = str(input("Deseja cadastrar uma nova palavra? \nS ou s para (Sim) ou qualquer outra letra para (Não)"))
      print ( "\n"  * 80 )
  #Opção do menu que leva ao codigo do Jogo da Forca
  elif (opcao == "forca"):
    finalPrograma = "s"
    while (finalPrograma == "S" or finalPrograma == "s"):
      #Transforma as palavras da listPalavras em uma lista dentro da lista palavraSecreta e palavraSecretaTraço
      if (n < len(listPalavras)):
        palavraSecreta = list((listPalavras[n]))
        palavraSecretaTraço = list((listPalavras[n]))
        vira = 0
        quantidadeLetras = 0
        saida = len(palavraSecreta)
      #Transforma as letras da lista palavraSecretaTraço em traços para exibição
      while vira < saida:
        if ((palavraSecreta[vira]) != ' '):
          palavraSecretaTraço[vira] = "._."
          quantidadeLetras = quantidadeLetras + 1
        vira = vira + 1
      #Inicia o jogo com 0 erros
      erro = 0
      while (erro < 6):
        #Pula 80 linhas e inicia a interface do jogo
        print ( "\n"  * 80 )
        print('''
JOGO DA FORCA

Regras:
-Só é possivel informar uma (1) letra por rodada
-Você tem direito de arriscar um (1) palpite a cada rodada
-Se você errar até seis (6) vezes as letras digitadas, o jogo acaba
-Se você errar o palpite, o jogo acaba
-Se você acertar todas as palavras o jogo acaba
-Digite (quit) para sair do Jogo da Forca
--------------------------------------------------------------------

- Palavra número {} de {} -

A palavra tem {} letras
Dica: {}
'''.format(n+1, len(listPalavras), quantidadeLetras, listDicas[n]))
        #Laço para mostrar as letras digitadas ao usuario
        x = 0
        print("Letras digitadas: ", end="")
        while (x < len(letrasDigitadas)):
          print(letrasDigitadas[x], end=" - ")
          x = x + 1        
        #If's com as 6 opçoes de erro, com alteração do boneco (Altera a cor de um menbro do boneco a cada erro para vermelho))
        if (erro == 0):
          print("\n")
          print("+-------+")
          print("|       |")
          print("|       O")
          print("|      /|\ ")
          print("|      / \ ")
          print("|          ")
          print("===================== \n")
        elif (erro == 1):
          print("\n")
          print("+-------+")
          print("|       |")
          print("|       O")
          print("|      /|\ ")
          print("|      / "+'\033[31m'+"\ "+'\033[0;0m')
          print("|")
          print("===================== \n")
        elif (erro == 2):
          print("\n")
          print("+-------+")
          print("|       |")
          print("|       O")
          print("|      /|\ ")
          print("|"+'\033[31m'+"      / \ "+'\033[0;0m')
          print("|")
          print("===================== \n")
        elif (erro == 3):
          print("\n")
          print("+-------+")
          print("|       |")
          print("|       O")
          print("|      /|"+'\033[31m'+"\ "+'\033[0;0m')
          print("|"+'\033[31m'+"      / \ "+'\033[0;0m')
          print("|")
          print("===================== \n")
        elif (erro == 4):
          print("\n")
          print("+-------+")
          print("|       |")
          print("|       O")
          print("|      "+'\033[31m'+"/"+'\033[0;0m'+"|"+'\033[31m'+"\ "+'\033[0;0m')
          print("|"+'\033[31m'+"      / \ "+'\033[0;0m')
          print("|")
          print("===================== \n")
        elif (erro == 5):
          print("\n")
          print("+-------+")
          print("|       |")
          print("|       O")
          print("|"+'\033[31m'+"      /|\ "+'\033[0;0m')
          print("|"+'\033[31m'+"      / \ "+'\033[0;0m')
          print("|")
          print("===================== \n")
        #Exibição da palavra em forma de traços
        final = "".join(palavraSecretaTraço)
        print(final, "\n")
        #Solicita uma letra ao usuário
        print("=====================")
        letraUsuario = input("\033[47m"+"\033[30m"+"\033[1m"+"Informe uma letra "+"\033[0;0m"+"\033[0;0m"+"\033[0;0m")
        print("=====================")
        print()
        #Testa se o usuario digitou quit para sair do jogo da forca
        if (letraUsuario == "quit"):
          erro = 6
          print ( "\n"  * 80 )
          break
        else:
        #Testa se o usuario digitou mais de uma letra ou se digitou algum numero          
          if (len(letraUsuario) > 1 or letraUsuario == "1" or letraUsuario == "2" or letraUsuario == "3" or letraUsuario == "4" or letraUsuario == "5" or letraUsuario == "6" or letraUsuario == "7" or letraUsuario == "8" or letraUsuario == "9" or letraUsuario == "0"):
            print("Por favor, digite apenas uma letra")          
          #Se ele digitou apenas uma letra
          else:
            #Adiciona a letra digitada na lista das Letras digitadas
            letrasDigitadas.append(letraUsuario.upper())
            vira = 0
            #Conta quantas letras (e espaços vazio) tem na lista palavraSecreta
            saida = len(palavraSecreta)
            #Testa se a letra digitada tem na lista de palavraSecreta e se tiver transforma o traço (_) da lista palavraSecretaTraço na letra digitada pelo usuario
            correto = 0
            while vira < saida:
              if ((palavraSecreta[vira]) == letraUsuario.upper()):
                palavraSecretaTraço[vira] = letraUsuario.upper()
                correto = 1
              vira = vira + 1
            #Testa de houve alguma letra certa na palavra, se não erro + 1
            if correto != 1:
              erro = erro + 1 
            #Imprimi a lista palavraSecretaTraço alterada com a letra digitada (Se tiver a letra digitada pelo usuario)
            final = "".join(palavraSecretaTraço)
            print(final)
            #Teste se tiver sido errado 6 vezes final do programa
            if (erro == 6):
              print("\n\nInfelizmente você errou as 6 vezes... Até a próxima")
              #Função (del) apaga todos os elementos da lista letrasDigitadas caso o usuario volte a jogar
              del letrasDigitadas[:]
              break            
            #Pergunta ao usuario se ele tem algum palpite da palavra correta sempre que ele 'chuta' uma nova letra
            print('\033[31m'+'''
  Deseja arriscar um palpite? 
  Digite S ou s para (Sim) ou qualquer outra letra para (Não)\n'''+'\033[0;0m')
            #Captura se o usuario quer arriscar o palpite (se ele digitou S ou s)
            palpite = input("\033[47m"+"\033[30m"+"\033[1m"+" Opção "+"\033[0;0m"+"\033[0;0m"+"\033[0;0m")
            print()
            #Caso tenha digitado S ou s (sim)
            if (palpite == "S" or palpite == "s"):
              #Pergunta qual o palpite da palavra correta, transforma o palpite em uma lista (palpiteResposta) e compara com a responsta correta que é a lista (palavraSecreta) 
              palpite = input("Qual o seu palpite?")
              palpiteResposta = list(palpite.upper())
              finalPrograma = "nn"
              #Se o papalpite estiver correto, ele informa 
              if (palpiteResposta == palavraSecreta):
                del letrasDigitadas[:]
                print('''
Parabéns, você acertou! A palavra era {}
Deseja continuar a jogar? 
Digite S ou s para (Sim), N ou n (Não)\n'''.format("".join(palavraSecreta)))
                #Pergunta se o usuario deseja continuar a jogar
                finalPrograma = input("\033[47m"+"\033[30m"+"\033[1m"+" Opção "+"\033[0;0m"+"\033[0;0m"+"\033[0;0m")              
                #Testa se o usuario deseja continuar jogando, caso sim, soma n = n + 1 para alterar a palavra da listPalavras
                if (finalPrograma == "S" or finalPrograma == "s"):
                  n = n + 1
                  #Testa se o usuario já jogou todas as palavras da listPalavras
                  if (n >= len(listPalavras)):
                    del letrasDigitadas[:]
                    print('''Você já descobriu todas as palavras. Obrigado por jogar!''')
                    #Declara erro = 6 para encerrar o programa
                    erro = 6
                    print ( "\n"  * 80 )
                  break
                #Se usuario não quiser continuar volta ao menu
                elif (finalPrograma == "N" or finalPrograma == "n"):
                  print ( "\n"  * 80 )
                  break
              #Caso o palpite esteja incorreto entra no else
              else:
                #Função (del) apaga os itens da lista letrasDigitadas caso o mesmo volte a jogar
                del letrasDigitadas[:]
                print("Palavra incorreta")
                #Declara erro = 6 para encerrar o programa
                erro = 6
                print ( "\n"  * 80 )
      #Caso o erro seja igual a 6 o jogo é encerrado e retorna para o menu
      if (erro == 6):
         break      
  #Opção do menu que leva ao codigo de Perguntas e Respostas
  elif(opcao == "perguntas"):
    print("\nAdicionar o codigo do jogo das perguntas e respostas")
    break #RETIRAR O BREAK QUANDO ADICIONAR O CODIGO
  #Opção do menu que encerra todo o programa
  elif(opcao == "quit"):
    print("\nEncerramento da aplicação")
  #Caso usuario digite qualquer outra coisa sem ser as opções informadas, pula 80 linhas e retorna para o menu
  else:
    print ( "\n"  * 80 )

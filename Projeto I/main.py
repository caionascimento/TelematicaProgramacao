from funcoesProjeto import *
import random
import time

#Menu Inicial do Jogo
while (opcao != opcaoEncerrar):
  #Chama a função do Menu
  menu()
  opcao = input(opcaoBranco)
  #Chama a função de cadastro de palavras (senha: admin123)
  if (opcao == opcaoSuporte):
    while boleano:
      limparTela(0)
      print('''
Bem Vindo a área de Suporte ao Programa

Digite 1 para realizar um cadastro de palavra no Jogo da Forca
Digite 2 para realizar um cadastro de pergunta no Jogo das Perguntas
Digite {} para sair da área de suporte
'''.format(opcaoEncerrar))
      opcao = input(opcaoBranco)
      if opcao == '1':
        limparTela(0)
        cadastroPalavras()
      elif opcao == '2':
        limparTela(0)
        cadastroPerguntas()
      elif opcao == opcaoEncerrar:
        boleano = False
        opcao = 0
        limparTela(0)
      else:
        print("Por favor, informe uma opção valida!")
        limparTela(3)
  #Opção do menu que leva ao codigo do Jogo da Forca
  elif (opcao == opcaoForca):
    while True:
      #Transforma as palavras da listPalavras em uma lista dentro da lista palavraSecreta e palavraSecretaTraço
      if (numeroPalavra < len(listPalavras)):
        palavraSecreta = list((listPalavras[numeroPalavra]))
        palavraSecretaTraço = list((listPalavras[numeroPalavra]))
        quantidadeLetras = 0
      #Transforma as letras da lista palavraSecretaTraço em traços para exibição
      for i in range (len(palavraSecreta)):
        if ((palavraSecreta[i]) != ' '):
          palavraSecretaTraço[i] = "._."
          quantidadeLetras = quantidadeLetras + 1
      #Inicia o jogo com 0 erros
      erro = 0
      while (erro < quantErrosMaximo):
        #Pula 80 linhas e inicia a interface do jogo
        limparTela(0)
        regrasForca(numeroPalavra + 1, len(listPalavras), quantidadeLetras, listDicas[numeroPalavra])
        #Laço para mostrar as letras digitadas ao usuario
        print("Letras digitadas: ", end="")
        for i in range (len(letrasDigitadas)):
          print(letrasDigitadas[i], end=" - ")       
        #If's com as 6 opçoes de erro, com alteração do boneco (Altera a cor de um menbro do boneco a cada erro para vermelho))
        bonecosForca(erro)
        #Exibição da palavra em forma de traços
        final = "".join(palavraSecretaTraço)
        print(final, "\n")
        #Solicita uma letra ao usuário
        print("=====================")
        letraUsuario = input(letraBranco)
        print("=====================\n")
        #Testa se o usuario digitou o valor para sair do jogo da forca
        if (letraUsuario == opcaoEncerrar):
          erro = quantErrosMaximo
          limparTela(0)
          break
        else:
        #Testa se o usuario digitou mais de uma letra ou se digitou algum numero
          if (len(letraUsuario) > 1 or letraUsuario in opcoesInvalidasNum):
            print("Por favor, digite apenas uma letra")
            limparTela(2)
          #Se ele digitou apenas uma letra
          else:
            #Adiciona a letra digitada na lista das Letras digitadas
            letrasDigitadas.append(letraUsuario.upper())
            #Testa se a letra digitada tem na lista de palavraSecreta e se tiver transforma o traço (_) da lista palavraSecretaTraço na letra digitada pelo usuario
            correto = 0
            for i in range (len(palavraSecreta)):
              if ((palavraSecreta[i]) == letraUsuario.upper()):
                palavraSecretaTraço[i] = letraUsuario.upper()
                correto = 1
            #Testa de houve alguma letra certa na palavra, se não erro + 1
            if correto != 1:
              print("Infelizmente a letra '{}' não está nesta palavra". format(letraUsuario.upper()))
              erro = erro + 1 
            #Imprimi a lista palavraSecretaTraço alterada com a letra digitada (Se tiver a letra digitada pelo usuario)
            final = "".join(palavraSecretaTraço)
            print(final)
            #Teste se tiver sido errado 6 vezes final do programa
            if (erro == quantErrosMaximo):
              print("\n\nInfelizmente você errou as {} vezes... Até a próxima". format(quantErrosMaximo))
              limparTela(3)
              #Função (del) apaga todos os elementos da lista letrasDigitadas caso o usuario volte a jogar
              del letrasDigitadas[:]
            #Pergunta ao usuario se ele tem algum palpite da palavra correta sempre que ele 'chuta' uma nova letra
            print('\033[31m'+'''
Deseja arriscar um palpite? 
Digite S ou s para (Sim) ou qualquer outra letra para (Não)\n'''+'\033[0;0m')
            #Captura se o usuario quer arriscar o palpite (se ele digitou S ou s)
            palpite = input(opcaoBranco)
            #Caso tenha digitado S ou s (sim)
            if (palpite == "S" or palpite == "s"):
              #Pergunta qual o palpite da palavra correta, transforma o palpite em uma lista (palpiteResposta) e compara com a responsta correta que é a lista (palavraSecreta) 
              palpite = input("Qual o seu palpite?")
              palpiteResposta = list(palpite.upper())
              
              #Se o papalpite estiver correto, ele informa 
              if (palpiteResposta == palavraSecreta):
                del letrasDigitadas[:]
                print('''
Parabéns, você acertou! A palavra era {}

Deseja continuar a jogar? 
Digite S ou s para (Sim) ou qualquer outra letra para (Não)\n'''.format("".join(palavraSecreta)))
                #Pergunta se o usuario deseja continuar a jogar
                finalPrograma = input(opcaoBranco)              
                #Testa se o usuario deseja continuar jogando, caso sim, soma n = n + 1 para alterar a palavra da listPalavras
                if (finalPrograma == "S" or finalPrograma == "s"):
                  numeroPalavra = numeroPalavra + 1
                  #Testa se o usuario já jogou todas as palavras da listPalavras
                  if (numeroPalavra >= len(listPalavras)):
                    del letrasDigitadas[:]
                    print('''\nVocê já descobriu todas as palavras. Obrigado por jogar!''')
                    limparTela(3)
                    #Declara erro = 6 para encerrar o programa
                    erro = quantErrosMaximo
                  break
                #Se usuario não quiser continuar volta ao menu
                else:
                  limparTela(0)
                  break
              #Caso o palpite esteja incorreto entra no else
              else:
                #Função (del) apaga os itens da lista letrasDigitadas caso o mesmo volte a jogar
                del letrasDigitadas[:]
                print("Palavra incorreta")
                #Declara erro = 6 para encerrar o programa
                erro = quantErrosMaximo
                limparTela(3)
      #Caso o erro seja igual a 6 o jogo é encerrado e retorna para o menu
      if (erro == quantErrosMaximo):
         break
  #Opção do menu que leva ao codigo de Perguntas e Respostas
  elif(opcao == opcaoPerguntas):
    #Inicia um Loop passando por todas as perguntas cadastradas no dicionario
    limparTela(0)
    while True:
      regrasPerguntas()
      tresOpcoes = ['1', '2', '3']
      opcao = input(opcaoBranco)
      if opcao == opcaoEncerrar:
        opcao = 1
        limparTela(0)
        break
      elif opcao not in tresOpcoes:
        print("\nPor favor, passe uma opção valida!")
        limparTela(3)
      else:
        while True:
          if opcao == '1':
            acertos, erros, respondidas = 0, 0, 0
            a = list(range(1,len(perguntasF)+1))
            random.shuffle(a)
            for numPerg in a:
              while boleano:
                limparTela(0)
                print(fdVerde + ltNegrito + ' NÍVEL FACIL \n' + finalCor + finalCor)
                print('{} \n'.format(perguntasF[numPerg][0]))
                print('A) %s \n' % perguntasF[numPerg][1])
                print('B) %s \n' % perguntasF[numPerg][2])
                print('C) %s \n' % perguntasF[numPerg][3])
                print('D) %s \n' % perguntasF[numPerg][4])
                print('Qual a resposta correta? A B C ou D?\n')
                resposta = input(respostaBranco)
                #Grava quantas perguntas foram respondidas pelo usuario
                if resposta == opcaoEncerrar:
                  limparTela(0)
                  break
                if resposta.upper() not in opcoesValidasAltern or len(resposta) > 1:
                  print("\nPor Favor, informe apenas uma letra valida")
                  limparTela(3)
                else:
                  if (resposta.upper() == (perguntasF[numPerg][5])):
                    acertos = acertos + 1
                    respondidas = respondidas + 1
                  else:
                    erros = erros + 1
                    respondidas = respondidas + 1
                  break
              if resposta == opcaoEncerrar:
                break
            porcAcertos(acertos, respondidas, len(perguntasF))
            opcao = '2'
          elif opcao == '2':
            acertos, erros, respondidas = 0, 0, 0
            a = list(range(1,len(perguntasM)+1))
            random.shuffle(a)
            for numPerg in a:
              while boleano:
                limparTela(0)
                print(fdAmarelo + ltNegrito + ltPreto + ' NÍVEL MÉDIO \n' + finalCor + finalCor + finalCor)
                print('{} \n'.format(perguntasM[numPerg][0]))
                print('A) %s \n' % perguntasM[numPerg][1])
                print('B) %s \n' % perguntasM[numPerg][2])
                print('C) %s \n' % perguntasM[numPerg][3])
                print('D) %s \n' % perguntasM[numPerg][4])
                print('Qual a resposta correta? A B C ou D?\n')
                resposta = input(respostaBranco)
                #Grava quantas perguntas foram respondidas pelo usuario
                if resposta == opcaoEncerrar:
                  limparTela(0)
                  break
                if resposta.upper() not in opcoesValidasAltern or len(resposta) > 1:
                  print("\nPor Favor, informe apenas uma letra valida")
                  limparTela(3)
                else:
                  if (resposta.upper() == (perguntasM[numPerg][5])):
                    acertos = acertos + 1
                    respondidas = respondidas + 1
                  else:
                    erros = erros + 1
                    respondidas = respondidas + 1
                  break
              if resposta == opcaoEncerrar:
                break
            porcAcertos(acertos, respondidas, len(perguntasM))
            opcao = '3'
          elif opcao == '3':
            acertos, erros, respondidas = 0, 0, 0
            a = list(range(1,len(perguntasD)+1))
            random.shuffle(a)
            for numPerg in a:
              while boleano:
                limparTela(0)
                print(fdVermelho + ltNegrito + ' NÍVEL DIFÍCIO \n' + finalCor + finalCor)
                print('{} \n'.format(perguntasD[numPerg][0]))
                print('A) %s \n' % perguntasD[numPerg][1])
                print('B) %s \n' % perguntasD[numPerg][2])
                print('C) %s \n' % perguntasD[numPerg][3])
                print('D) %s \n' % perguntasD[numPerg][4])
                print('Qual a resposta correta? A B C ou D?\n')
                resposta = input(respostaBranco)
                #Grava quantas perguntas foram respondidas pelo usuario
                if resposta == opcaoEncerrar:
                  limparTela(0)
                  break
                if resposta.upper() not in opcoesValidasAltern or len(resposta) > 1:
                  print("\nPor Favor, informe apenas uma letra valida")
                  limparTela(3)
                else:
                  if (resposta.upper() == (perguntasD[numPerg][5])):
                    acertos = acertos + 1
                    respondidas = respondidas + 1
                  else:
                    erros = erros + 1
                    respondidas = respondidas + 1
                  break
              if resposta == opcaoEncerrar:
                break
            porcAcertos(acertos, respondidas, len(perguntasD))
            break
  #Opção do menu que encerra todo o programa
  elif(opcao == opcaoEncerrar):
    print("\nEncerramento da aplicação")
  #Caso usuario digite qualquer outra coisa sem ser as opções informadas, pula 80 linhas e retorna para o menu
  else:
    limparTela(0)









import time

#Tempo e limpeza de Tela
def limparTela(segundos): 
  time.sleep(segundos)
  print ("\n" * 80)

#Banco de Dados da Aplicação
listPalavras = ['WHILE', 'MKDIR', 'SUDO']
listDicas = ['Comando usado para repetição em linguagens de programação', 'Comando usado em Terminal Linux para criar um novo diretório', 'Comando usado em Terminal Linux para Verificar Permissões']

perguntasF = {1: ['QUANTO SAO 2+2?', '5', '7', '4', '2', 'C'],
2: ['O QUE ESTA ESCRITO NA BANDEIRA DO BRASIL?', 'ORDEM E REGRESSO', 'ORDEM E RETROCESSO', 'ORDEM E PROGRESSO', 'PROGRESSO E ORDEM', 'C'],
3: ['QUAL O SIGNIFICADO DA PALAVRA INGLESA "HORSE"?', 'CASA', 'CAVALO', 'ELEFANTE', 'HIPOPÓTAMO', 'B']
}

perguntasM = {1: ['QUANTOS ESTADOS POSSUI O BRASIL?', '20 ESTADOS', '25 ESTADOS', '27 ESTADOS', '30 ESTADOS', 'C'],
2: ['QUAL O NOME DA ESCALA QUE MEDE A MAGNITUDE DOS TERREMOTOS?', 'ESCALA RICHMOR', 'ESCALA SISMICA', 'ESCALA TERMICA', 'ESCALA RICHTER', 'D'],
3: ['QUAL E A CAPITAL DE BRASILIA?', 'BRASIL', 'DISTRITO NACIONAL', 'DISTRITO FEDERAL', 'PLANO PILOTO', 'C']
}

perguntasD = {1: ['QUEM FOI O COMPOSITOR DA MUSICA DO HINO NACIONAL BRASILEIRO?', 'MACHADO DE ASSIS', 'DOM PEDRO I', 'JOAQUIM OSORIO DUQUE ESTRADA', 'FRANCISCO MANOEL DA SILVA', 'C'],
2: ['NOME DO MORRO EM QUE SE ENCONTRA A ESTATUA DO CRISTO REDENTOR?', 'MORRO DO PAO DE ACUCAR', 'MORRO DO CORCOVADO', 'MORRO DA GUANABARA', 'MORRO DO REDENTOR', 'A'],
3: ['QUAL E O SIGNIFICADO DA PALAVRA MISCIGENACAO?', 'PESSOA INGENUA', 'MISTURA DE VARIADAS COMPILACOES LITERARIAS', 'CRUZAMENTO INTER-RACIAL', 'DOENCA QUE ATINGE A PELE', 'C']
}

#Cores para Letras
ltVermelho = '\033[31m'
ltVerde = '\033[32m'
ltAzul = '\033[34m'
ltCiano = '\033[36m'
ltMagenta = '\033[35m'
ltAmarelo = '\033[33m'
ltPreto = '\033[30m'
ltBranco = '\033[37m'
ltNegrito = '\033[1m'

#Cores de Fundo
fdPreto = '\033[40m'
fdVermelho = '\033[41m'
fdVerde = '\033[42m'
fdAmarelo = '\033[43m'
fdAzul = '\033[44m'
fdMagenta = '\033[45m'
fdCiano = '\033[46m'
fdBranco = '\033[47m'

#Sempre colocar a cor final para fechar
finalCor = '\033[0;0m'

#Textos Pintados
opcaoBranco = fdBranco + ltPreto + ltNegrito + " Opção " + finalCor + finalCor + finalCor
respostaBranco = fdBranco + ltPreto + ltNegrito + " Resposta " + finalCor + finalCor + finalCor
letraBranco = fdBranco + ltPreto + ltNegrito + " Informe uma letra " + finalCor + finalCor + finalCor

#Variaveis Globais
#Chaves de acesso
opcaoEncerrar = "quit"
opcaoSuporte = "admin123"
opcaoForca = "forca"
opcaoPerguntas = "perguntas"
quantErrosMaximo = 6

#Variaveis para funcionamento do codigo
boleano = True
numeroPalavra = 0
opcao = "inicio"
#correto = 0
finalPrograma = "s"
letrasDigitadas = []

#Validação de entrada da Forca
opcoesInvalidasNum =  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#Validação de entrada das Perguntas
opcoesValidasAltern = ["A", "B", "C", "D"]

#Menu
def menu():
  limparTela(0)
  print('''
{0}{1}{3}                           Bem vindo a Plataforma                           {2}{2}{2}

{0}{1}{3} Digite (forca) para iniciar o Jogo da Forca                                {2}{2}{2}
{0}{1}{3} Digite (perguntas) para iniciar o Jogo de Perguntas e Respostas            {2}{2}{2}
{0}{1}{3} Digite ({4}) para encerrar a Plataforma Multijogos                        {2}{2}{2}
{0}{1}{3} Digite a senha para configurar a Plataforma Multijogos                     {2}{2}{2}
'''.format(fdCiano, ltPreto, finalCor, ltNegrito, opcaoEncerrar))

#Regras da Forca
def regrasForca(numPalava, totalPalavras, quantiaLetras, dica):
  print('''
{0}{1}{3}                              JOGO DA FORCA                                {2}{2}{2}

{0}{1}{3}                                  Regras:                                  {2}{2}{2}
{0}{1}{3} -Só é possivel informar uma (1) letra por rodada                          {2}{2}{2}
{0}{1}{3} -Você tem direito de arriscar um (1) palpite a cada rodada                {2}{2}{2}
{0}{1}{3} -Se você errar até seis (6) vezes as letras digitadas, o jogo acaba       {2}{2}{2}
{0}{1}{3} -Se você errar o palpite, o jogo acaba                                    {2}{2}{2}
{0}{1}{3} -Se você acertar todas as palavras o jogo acaba                           {2}{2}{2}
{0}{1}{3} -Digite {4} para sair do Jogo da Forca                                   {2}{2}{2}

- Palavra número {5} de {6} -

A palavra tem {7} letras
Dica: {8}
'''.format(fdCiano, ltPreto, finalCor, ltNegrito, opcaoEncerrar, numPalava, totalPalavras, quantiaLetras, dica))

#Cadastro de Palavras 
def cadastroPalavras():
  saida = "s"
  limparTela(0)
  #Solicita a PALAVRA e a DICA para cadastro
  while (saida == 's' or saida == 'S'):
    print(" - Cadastro de palavras - \n")
    novaPalavra = str(input("Informe a nova palavra:"))
    novaDica = str(input("Informe a dica da palavra:"))
    #Confirmação se a palavra e dica estão corretas para cadastro
    print('''
Se você realmente deseja cadastrar as informações a baixo, digite (ok)
Palavra: {}
Dica: {}
'''.format(novaPalavra, novaDica))
    cadastro = input(opcaoBranco)
    #Teste se realmente o usuario vai cadastrar a PALAVRA e a DICA passada
    if (cadastro == "ok" or cadastro == "OK"):
      listPalavras.append(novaPalavra.upper())
      listDicas.append(novaDica)
      print("Palavra e Dica cadastradas com sucesso!\n")
    else: 
      print("Palavra e Dica não cadastradas")
    #Pergunta se deseja cadastrar mais palavras na lista
    saida = str(input("Deseja cadastrar uma nova palavra? \nS ou s para (Sim) ou qualquer outra letra para (Não)"))
    if saida != "s" or saida != "S":
      boleano = False
    limparTela(0)

#Pintura dos Bonecos
def bonecosForca(erro):
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
    print("|      / "+ltVermelho+"\ "+finalCor)
    print("|")
    print("===================== \n")
  elif (erro == 2):
    print("\n")
    print("+-------+")
    print("|       |")
    print("|       O")
    print("|      /|\ ")
    print("|"+'\033[31m'+"      / \ "+finalCor)
    print("|")
    print("===================== \n")
  elif (erro == 3):
    print("\n")
    print("+-------+")
    print("|       |")
    print("|       O")
    print("|      /|"+ltVermelho+"\ "+finalCor)
    print("|"+ltVermelho+"      / \ "+finalCor)
    print("|")
    print("===================== \n")
  elif (erro == 4):
    print("\n")
    print("+-------+")
    print("|       |")
    print("|       O")
    print("|      "+ltVermelho+"/"+finalCor+"|"+ltVermelho+"\ "+finalCor)
    print("|"+ltVermelho+"      / \ "+finalCor)
    print("|")
    print("===================== \n")
  elif (erro == 5):
    print("\n")
    print("+-------+")
    print("|       |")
    print("|       O")
    print("|"+ltVermelho+"      /|\ "+finalCor)
    print("|"+ltVermelho+"      / \ "+finalCor)
    print("|")
    print("===================== \n")
  elif (erro == 6):
    print("\n")
    print("+-------+")
    print("|       |")
    print("|"+ltVermelho+"       O  "+finalCor)
    print("|"+ltVermelho+"      /|\ "+finalCor)
    print("|"+ltVermelho+"      / \ "+finalCor)
    print("|")
    print("===================== \n")

#Regras das Perguntas
def regrasPerguntas():
  print('''
{0}{1}{4}                            JOGO DAS PERGUNTAS                             {2}{2}{2}

{0}{1}{4}                                  Regras:                                  {2}{2}{2}
{0}{1}{4} -Você pode escolher qual o nível das perguntas deseja jogar               {2}{2}{2}
{0}{1}{4} -Você só pode escolher uma alternativa das 4 disponiveis em cada pergunta {2}{2}{2}
{0}{1}{4} -Ao Final de cada Nível, você jogara o próximo nível                      {2}{2}{2}
{0}{1}{4} -Digite {3} para sair do Jogo das Perguntas                              {2}{2}{2}

- Informe qual nível deseja jogar -

Digite 1 para FÁCIL
Digite 2 para MÉDIO
Digite 3 para DIFÍCIL
'''.format(fdCiano, ltPreto, finalCor, opcaoEncerrar, ltNegrito))

#Cadastro de Perguntas
def cadastroPerguntas():
  saida = "s"
  limparTela(0)
  while (saida == 's' or saida == 'S'):
    print(" - Cadastro de perguntas - \n")
    novoNivel = str(input("Informe o nível da pergunta, 1 para Facil, 2 para Médio e 3 para Difícil"))
    niveisLegiveis = ["1", "2", "3"]
    if novoNivel in niveisLegiveis:
      novaPergunta = str(input("Informe a nova pergunta:"))
      novaAlternativaA = str(input("Informe a resposta para a alternativa A:"))
      novaAlternativaB = str(input("Informe a resposta para a alternativa B:"))
      novaAlternativaC = str(input("Informe a resposta para a alternativa C:"))
      novaAlternativaD = str(input("Informe a resposta para a alternativa D:"))
      novaResposta = str(input("Informe qual é a alternativa correta para a sua pergunta:"))
      print('''
Se você realmente deseja cadastrar as informações a baixo, digite (ok)

Nível: {}
Pergunta: {}
Alternativa A: {}
Alternativa B: {}
Alternativa C: {}
Alternativa D: {}
Resposta Correta: {}
    '''.format(novoNivel, novaPergunta, novaAlternativaA, novaAlternativaB, novaAlternativaC, novaAlternativaD, novaResposta))
      cadastro = input(opcaoBranco)
      if (cadastro == "ok" or cadastro == "OK"):
        if novoNivel == "1":
          perguntasF[len(perguntasF)+1] = [novaPergunta.upper(), novaAlternativaA.upper(), novaAlternativaB.upper(), novaAlternativaC.upper(), novaAlternativaD.upper(), novaResposta.upper()]
        elif novoNivel == "2":
          perguntasM[len(perguntasM)+1] = [novaPergunta.upper(), novaAlternativaA.upper(), novaAlternativaB.upper(), novaAlternativaC.upper(), novaAlternativaD.upper(), novaResposta.upper()]
        elif novoNivel == "3":
          perguntasD[len(perguntasD)+1] = [novaPergunta.upper(), novaAlternativaA.upper(), novaAlternativaB.upper(), novaAlternativaC.upper(), novaAlternativaD.upper(), novaResposta.upper()]
        print("Perguntas e Respostas foram cadastradas com sucesso!\n")
      else: 
        print("Perguntas e Respostas não cadastradas")
      #Pergunta se deseja cadastrar mais palavras na lista
      saida = str(input("Deseja cadastrar uma nova pergunta? \nS ou s para (Sim) ou qualquer outra letra para (Não)"))
      limparTela(0)
    else:
      print("Por favor, informe o nivel correto")
      limparTela(3)

#Calculo de Acertos de Perguntas
def porcAcertos(acertos, respondidas, operador):
  limparTela(0)
  print("Você respondeu {} de {} perguntas".format(respondidas, operador))
  #Imprimi na tela uma barra colorida de acordo com o percentual de acerto 
  porcentagemAcerto = int((acertos * 100)/operador)
  print('Seu Percentual de acerto foi de {0:.2f} % '.format(porcentagemAcerto))
  if (porcentagemAcerto < 50):
    print(('\033[41m'+' '+'\033[0;0m') * int(porcentagemAcerto/2))
  elif (porcentagemAcerto >= 50 and porcentagemAcerto <= 70):
    print(('\033[43m'+' '+'\033[0;0m') * int(porcentagemAcerto/2))
  elif (porcentagemAcerto > 70):
    print(('\033[42m'+' '+'\033[0;0m') * int(porcentagemAcerto/2))
  limparTela(3)
  
  
  
  
  
  
  
  
  
  
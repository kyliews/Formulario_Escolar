cod_alunoD = {}
banco_notas = {}
lista_notas = []
banco_medias = {}

def cadastrar_aluno():

  cod_aluno = input("Digite um código numérico para o aluno: ")
  nome_aluno = input("Digite o nome do aluno:")
  nota1 = float(input("Digite a primeira nota do aluno:"))
  nota2 = float(input("Digite a segunda nota do aluno:"))
  nota3 = float(input("Digite a terceira nota do aluno:"))
  media = (nota1 + nota2 + nota3) / 3
  global lista_notas 
  lista_notas.append(nota1)
  lista_notas.append(nota2)
  lista_notas.append(nota3)

  cod_alunoD[cod_aluno] = nome_aluno
  banco_notas[cod_aluno] = lista_notas
  banco_medias[cod_aluno] = media
  lista_notas = []
  print('O aluno cadastrado foi {} e a suas notas estão no sistema.'.format(nome_aluno))

def mostrar_alunos():
  print("Lista de alunos cadastrados:")
  print("-----------------------------")
  print(cod_alunoD)

def mostrar_notas():
  print(cod_alunoD)
  Cod_Aluno = input("Digite o cod de cadastro do aluno: ")
  nome_aluno = cod_alunoD.get(Cod_Aluno)
  notas = banco_notas.get(Cod_Aluno)
  media = banco_medias.get(Cod_Aluno)

  print("As notas do aluno {} são: {}".format(cod_alunoD.get(Cod_Aluno),notas))
  print("E sua média é: {}".format(media))



while True:

    print("0 - CADASTRAR ALUNO \n1 - MOSTRAR CADASTROS \n2 - MOSTRAR NOTA")

    conf = int(input("Digite sua opção: "))

    if (conf == 0): 
        cadastrar_aluno()

    elif (conf == 1):  
        mostrar_alunos()

    elif (conf == 2):  
        mostrar_notas()

    print("")
    print("===========")
    print("0 para CONTINUAR | 1 para SAIR")
    if int(input()) == 1:
        break
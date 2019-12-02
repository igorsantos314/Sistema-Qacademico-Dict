import os.path
from tkinter import *

alunos = {}

def inserir(cpf, nome) :
  alunos[cpf] = (nome, {})
  inserirBD(cpf, nome)

def inserirBD(cpf, nome):
  if os.path.exists(str(cpf)) == False:
    arqUser = open('BD/{}'.format(str(cpf)),'w', encoding='latin-1')
    
    conteudo = '{}'.format(nome)

    arqUser.write(conteudo)
    arqUser.close()

def lerBD():
  arqs = [nome for nome in os.listdir('BD/')]
  
  for i in arqs:
    arqAtual = open('BD/{}'.format(str(i)), 'r', encoding='latin-1')

    user = arqAtual.readlines()

    cpf = int(i)
    nome = user[0].replace('\n','')
    disciplinas = []

    inserir(cpf, nome)

    for linhas in user:
      disciplinas.append(linhas)

    pos = 0

    quantidade = int( (len(disciplinas)-1) / 3 )
    #print(disciplinas)
    #print(quantidade)

    for elemento in range(quantidade):
      codDisc = int(disciplinas[pos+1])
      nomeDisc = disciplinas[pos+2].replace('\n','')
      semestreDisc = disciplinas[pos+3].replace('\n','')

      cadastrarDisciplina(cpf, codDisc, nomeDisc, semestreDisc)
      pos += 3

    arqAtual.close()

def estaRegistrado(cpf) :
  if cpf in alunos :
    return alunos[cpf]
  return ()

def remover(cpf) :
  if cpf in alunos :
    del alunos[cpf]

def cadastrarDisciplina(cpf, codigo, nomeDisciplina, semestre) :
  aluno = estaRegistrado(cpf)
  if aluno != () :
    disciplinasCursadas = aluno[1]
    disciplinasCursadas[codigo] = (nomeDisciplina, semestre)
    
    if jaCursou(cpf, codigo) == False:
      print('Existe')
    else:
      inserirDisciplinaBD(cpf, codigo, nomeDisciplina, semestre)

def inserirDisciplinaBD(cpf, codigo, nomeDisciplina, semestre):
  arqUser = open('BD/{}'.format(str(cpf)),'a', encoding='latin-1')
  
  conteudo = '\n{}\n{}\n{}'.format(codigo, nomeDisciplina, semestre)

  arqUser.write(conteudo)
  arqUser.close()

def jaCursou(cpf, codigo) :
  cursou = False
  aluno = estaRegistrado(cpf)
  if aluno != () and codigo in aluno[1] : 
    cursou = True
  return cursou
"""
def removeUltimo(str) :
  if len(str) > 0 and str[len(str) - 1] == '\n':
    return str[0:len(str)-1]
  else :
    return str

def AlerBD(arquivo):
  f = open(arquivo, 'r')
  conteudo = f.readlines()
  bdAlunos = {}
  temp = []
  for x in conteudo :
    temp.append(removeUltimo(x))

  conteudo = temp
    
  i = 0
  while i < len(conteudo) :
    if (i + 2  < len(conteudo)) :
      cpf = conteudo[i]
      nome = conteudo[i+1]
      bdAlunos[cpf] = (nome, {})
      qtdDisciplinas = int(conteudo[i+2])
      i = i + 3
      ultimaPosicao = (i + (qtdDisciplinas * 3)) - 1
      while i <= ultimaPosicao:
        codigoDisciplina = conteudo[i]
        nomeDisciplina = conteudo[i+1]
        semestreDisciplina = conteudo[i+2]
        bdAlunos[cpf][1][codigoDisciplina] = (nomeDisciplina, semestreDisciplina)
        i = i + 3

  f.close()     
  return bdAlunos
"""
def consultarAluno(cpf):
  aluno = alunos[cpf]

  print(aluno)

def constructWindow():
  global janela
  global btCadastrar
  global btConsultar
  global btVincularDisciplina
  global btEditar

  janela = Tk()
  janela.geometry('200x250')
  janela.title('KA')

  lblTitle = Label(janela, text='KAcadêmico', font='Arial 12 bold', width=15)
  lblTitle.pack()

  btCadastrar = Button(janela, text='Cadastrar Discente', width=15, command=cadastroInterface)
  btCadastrar.pack()

  btConsultar = Button(janela, text='Consultar Discente', width=15, command=consultaInterface)
  btConsultar.pack()

  btVincularDisciplina = Button(janela, text='Vincular Disciplina', width=15, command=vinculoInterface)
  btVincularDisciplina.pack()

  btEditar = Button(janela, text='Editar Discente', width=15)
  btEditar.pack()

  janela.mainloop()

# ---------------------------------- CHAMANDO INTERFACES ----------------------------------
def cadastroInterface():
  global janela
  janela.destroy()

  janelaCadastro = Tk()
  janelaCadastro.geometry('300x200')
  janelaCadastro.title('Cadastrar Discente')

  #botoes de sair e menu
  btSair = Button(text='Sair', command=constructWindow)
  btSair.place(x=230, y=160)

  janelaCadastro.mainloop()

def consultaInterface():
  global janela
  janela.destroy()

  janelaConsulta = Tk()
  janelaConsulta.geometry('300x200')
  janelaConsulta.title('Consultar Discente')

  janelaConsulta.mainloop()

def vinculoInterface():
  global janela
  janela.destroy()

  janelaVincular = Tk()
  janelaVincular.geometry('300x200')
  janelaVincular.title('Vincular Disciplina')

  janelaVincular.mainloop()
# ---------------------------------- CHAMANDO INTERFACES ----------------------------------

def main():
  print('====================================')
  print(' 1 - Cadastrar Aluno')
  print(' 2 - Consultar Aluno')
  print(' 3 - Vincular Disciplina ao Aluno')
  print(' 4 - Editar Aluno')
  print(' 5 - SAIR')
  print('====================================')

  try:
    opc = int(input('>> Informe a Opcao: '))

    if opc == 1:
      try:
        cpf = int(input('Informe o CPF: '))

        if estaRegistrado(cpf) != ():
          print('\n J Á  E S T Á  R E G I S T R A D O ')

        else:
          nome = input('>> Informe o nome: ')
          inserir(cpf, nome)

          print('\n C A D A S T R A D O !')

      except ValueError:
        print('D I G I T E  A P E N A S  N Ú M E R O S')


    elif opc == 2:
      try:
        cpf = int(input('Informe o CPF: '))

        if estaRegistrado(cpf) != ():
          consultarAluno(cpf)

        else:
          print('I N E X I S T E N T E')

      except ValueError:
        print('D I G I T E  A P E N A S  N Ú M E R O S')

    elif opc == 3:
      try:
        cpf = int(input('Informe o CPF: '))

        if estaRegistrado(cpf) != ():
          codigo = int(input('>> Codigo Disciplina: '))
          nome = input('>> Nome Disciplina: ')
          semestre = input('>> Semestre: ')

          cadastrarDisciplina(cpf, codigo, nome, semestre)

        else:
          print('I N E X I S T E N T E')

      except ValueError:
        print('D I G I T E  A P E N A S  N Ú M E R O S')

    elif opc == 5:
      return True

    else:
      print(' O P Ç Ã O  I N V Á L I D A  !')

  except ValueError:
    print('D I G I T E  A P E N A S  N Ú M E R O S')

lerBD()
#print(alunos)
#constructWindow()

while True:
  if main():
    break
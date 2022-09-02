class Aluno:
  def __init__(self, nome, idade, matricula, curso, periodo):
    self.nome = nome
    self.matricula = matricula
    self.curso = curso
    self.periodo = periodo
    print(f'Nome: {nome}\nIdade: {idade}\nMatríucula: {matricula}\nCurso: {curso}\nPeríodo: {periodo}')
    print('_-'*30)

for i in range(2):
  nome_aluno = input('Nome? ')
  idade_aluno = int(input('Idade? '))
  matricula_aluno = input('Matrícula? ')
  curso_aluno = input('Curso? ')
  periodo_aluno = int(input('Período? '))
  aluno1 = Aluno(nome_aluno, idade_aluno, matricula_aluno, curso_aluno, periodo_aluno)
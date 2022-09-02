from Aluno import Aluno

if __name__ == "__main__":
  aluno1 = Aluno(20221370027, 'Alic', [10.0, 8.0, 7.0])
  print('Aluno: ', aluno1.nome)
  print('Matricula: ', aluno1.matricula)
  print('Notas: ', aluno1.notas)
  print('Media: ', aluno1.media())
  print()
  aluno1.nome = 'Aliclic'
  print(aluno1.nome)
  aluno1.adiciona_nota(9)
  print(aluno1.notas)
  print(aluno1.media())

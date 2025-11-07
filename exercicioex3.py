soma = 0
contador = 0
while True:
  # captura a nota
  nota = float(input("Digite a nota do aluno [notas negativas para sair]:"))
  # verifica se é negativo para encerrar e calcular a media
  if nota < 0:
    media = soma/contador
    print(f"A media dos {contador} alunos da turma é {round(media, 2)}!")
    print("Programa encerrado!")
    # encerra loop while
    break
  # adiciona cada nova nota a variavel soma
  soma += nota
  # icrementa o contador de notas
  contador += 1
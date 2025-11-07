op ="S"

while op == "S":
  dividendo = int(input("Informe o dividendo:"))

  while True:
    divisor = int(input("Informe o divisor"))
    if divisor == 0:
      print("Valor inválido!")
    else:
      break
  print(f"O valor da divisã de {dividendo} por {divisor} é {dividendo/divisor}")

  while True:
    op = input("Você deseja fazer um novo cálculo? (S/N)").upper()
    if op == "N":
      print("Programa encerrado")
      break
    elif op == "S":
      break
    else:
      print("Comando Inválido!")
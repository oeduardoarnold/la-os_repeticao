SENHA_CORRETA = 1234
senha_digitada = 0
tentativas = 0

while senha_digitada != SENHA_CORRETA:
    tentativas = tentativas + 1
    senha_digitada = int(input(f"Tentativa {tentativas}: Digite a senha: "))

    if senha_digitada != SENHA_CORRETA:
        print("ACESSO NEGADO")

print(f"ACESSO PERMITIDO (Número de tentativas: {tentativas})")
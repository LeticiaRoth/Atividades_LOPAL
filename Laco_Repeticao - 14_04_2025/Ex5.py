tentativas = 3
senha = str(input("Digite a senha:"))

while True:
    confirme = str(input("\nDigite a senha para entrar na sua conta:"))

    if senha == confirme:
        print("Senha correta!")
        break

    else:
        tentativas -= 1
        print(f"Senha incorreta, restam {tentativas} tentativas")


    if tentativas == 0:
        print("\nAcesso bloqueado!")
        break


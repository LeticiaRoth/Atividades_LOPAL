while True:
    senha = str(input("Digite a sua senha:"))
    confime = str(input("Confime sua senha:"))

    if senha == confime:
        print("Senha correta")
        break
    else:
        print("\nSenha incorreta")
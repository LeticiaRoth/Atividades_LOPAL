n1 = float (input("Digite o primeiro número:"))
n2 = float (input("Digite o segundo número:"))
opcao = input("\n1- Multiplicação: * \n2- Adição: + \n3- Subtração: - \n4- Divisão: /")

if opcao == "*":
    multiplicação = n1 * n2
    print(f"O resultado é: {multiplicação:.2f}")


elif opcao == "+":
    adicao = n1 + n2
    print(f"O resultado é: {adicao:.2f}")


elif opcao == "-":
    subtracao = n1 - n2
    print(f"O resultado é: {subtracao:.2f}")


elif opcao == "/":
    divisao = n1 / n2
    print(f"O resultado é: {divisao:.2f}")

else:
    print(f"Inválido")
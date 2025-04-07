quantidade = int(input("Digite a quantidade de produtos: "))
valor = float(input("Digite o valor do produto: "))


if quantidade > 100:
    desconto = valor * 0.1
    valorFinal = quantidade * (valor - desconto)


    print(f"\nValor inicial: {valor}")

    print(f"Quantidade solicitada: {quantidade}")

    print(f"Desconto por unidade: {desconto}")

    print(f"Valor final: {valorFinal}")


else:

    desconto = valor * 0.05
    valorFinal = quantidade * (valor - desconto)


    print(f"\nValor inicial: {valor}")

    print(f"Quantidade solicitada: {quantidade}")

    print(f"Desconto por unidade: {desconto}")

    print(f"Valor final: {valorFinal}")
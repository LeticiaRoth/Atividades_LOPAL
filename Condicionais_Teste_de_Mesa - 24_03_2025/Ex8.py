lado1 = int (input("Digite o valor do primeiro lado:"))
lado2 = int (input("Digite o valor do segundo lado:"))
lado3 = int (input("Digite o valor do terceiro lado:"))
lado4 = int (input("Digite o valor do quarto lado:"))


if lado1 == lado2 and lado1 == lado3 and lado1 == lado4:
    print(f"Quadrado")

elif lado1 == lado3 and lado2 == lado4:
    print(f"Retângulo")

else:
    print(f"Nenhum dos dois")
quantidade = 0

for n in range (1,11):
    numero = int(input(f"Digite o {n} número:"))

    if numero % 3 == 0:
        quantidade = quantidade + 1

print(f"\nNúmeros de múltplos de 3: {quantidade}")





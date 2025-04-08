lista_pares = []
lista_impar = []

for n in range (1, 11):
    numeros = int(input(f"Digite o {n}° número: "))

    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impar.append(numeros)

print("\nNúmeros pares:", lista_pares)
print("Números ímpares", lista_impar)


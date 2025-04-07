n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print(f"Primeiro número é negativo: ({n1})" * (n1 < 0) or f"Segundo número é negativo: ({n2})" * (n2 < 0) or f"Nenhum dos números é negativo")
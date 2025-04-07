nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


if nota1 <= nota2 and nota1 <= nota3:
    media = (nota2 + nota3) / 2

elif nota2 <= nota1 and nota2 <= nota3:
    media = (nota1 + nota3) / 2

else:
    media = (nota1 + nota2) / 2
    print(f"Média: {media:.2f}")
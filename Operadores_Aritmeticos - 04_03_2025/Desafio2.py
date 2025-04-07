capital = float(input("Digite o seu capital: "))
taxa = float(input("Digite a taxa de juros: ")) / 100
tempo = int(input("Digite o tempo: "))

montante = capital * (1 + taxa) ** tempo
print(f"O montante final depois de {tempo} é {montante:.2f}")
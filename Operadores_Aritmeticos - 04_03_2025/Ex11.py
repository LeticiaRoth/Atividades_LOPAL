peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))

imc = peso / (altura ** 2)
print(f"IMC é: {imc:.2f}")
num1 = int(input("Digite o primeiro número:")) 
num2 = int(input("Digite o segundo número:"))

print("Números pares." * (num1 % 2 == 0 and num2 % 2 == 0) or "Número impares.")
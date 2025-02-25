
#Exercício 1 #
n1 = int (input ("Digite o primeiro número:"))
n2 = int (input ("Digite o segundo número:"))

resultado = n1 + n2
print(f"O resultado é: {resultado}")


#Exercício 2 #
num = int (input("Digite um número:"))
nprimo = num % 2 != 0

print("O número é primo?",nprimo )



#Exercício 3 #
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

print(n1 > n3)
print(n2 < n4)



#Exercício 4 #
num = int(input("Digite um número: "))
print(abs(num))



#Exercício 5 #
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
print("Números pares."
      *
      (num1 % 2 == 0 and num2 % 2 == 0)
      or
      "Número impares.")



#Exercício 6 #
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(f"Primeiro número é negativo:  ({n1})" * (n1 < 0) or
      f"Segundo número é negativo: ({n2})" * (n2 < 0) or
      f"Nenhum dos números é negativo")



#Exercício 7#

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o segundo número:"))
media = num1 + num2 + num3 / 3
print(f"A média das notas: {media:.2f}")


#Exercício 8#
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
print(num1 + 15 == num2 * 3)



#Exercício 9#
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
divisao = num1 / num2
print(f"O resultado é: {divisao}")
resto = num1 % num2
print(f"O resto é: {resto}")


#Exercício 10#
tempC = float(input("Digite a temperatura em Celsius:"))
tempF = (9 / 5) * tempC + 32
print(f"A temperatura em Fahrenheit é: {tempF} ")


#Exercício 11#
peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))
imc = peso / (altura ** 2)
print(f"IMC é: {imc:.2f}")


#Exercício 12#
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
media_ponderada = ((n1 * 6) + (n2 * 4) + (n3 * 5)) / (6 + 4 + 5)
print(f"A média ponderada é: {media_ponderada:.2f}")


#Exercício 13#
num = int(input("Digite o número: "))
expoente = int(input("Digite o expoente: "))
potencia = num ** expoente
print(f"O resultado é: {potencia}")


#Desafio 1#
num = float(input("Digite o número: "))
raiz = num ** (1 / 3)
print(f"A raíz cúbica é: {raiz:.2f}")


#Desafio 2#
capital = float(input("Digite o seu capital: "))
taxa = float(input("Digite a taxa de juros: ")) / 100
tempo = int(input("Digite o tempo: "))
montante = capital * (1 + taxa) ** tempo
print(f"O montante final depois de {tempo} é {montante:.2f}")



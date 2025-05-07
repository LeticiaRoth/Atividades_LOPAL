def calculo_fatorial(numero):
    resultado = 1
    for i in range (2, numero + 1):
        resultado *= i
    return resultado
    
numero= int(input("Digite o número:"))
print(f"Fatorial de {numero}! é {calculo_fatorial(numero)}")
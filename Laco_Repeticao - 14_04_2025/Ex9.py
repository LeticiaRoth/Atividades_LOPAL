numeros = []


numeros_entrada = int(input("Digite um número (ou 0 para encerrar): "))

while numeros_entrada > 0:
    numeros.append(numeros_entrada)
    numeros_entrada = int(input("Digite um número (ou 0 para encerrar): "))


if numeros == []: # VVerifica se a lista está vazia e dá uma mensagem de erro
    print("ERRO - Digite uma sequência de números positivos!")
else:
  
    soma = 0
    contador = 0
    for num in numeros:
        soma += num
        contador += 1
    media = soma / contador

   
    menores_numeros = 0
    for num in numeros:
        if num < media:
            menores_numeros += 1

    print(f"\nMédia: {media:.2f}")
    print(f"Quantidade de números menores que a média: {menores_numeros}")

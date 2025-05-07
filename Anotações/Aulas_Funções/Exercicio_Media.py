def calculo_media():
    lista = []
    quantidade = int(input("Digite a quantidade de números:"))
    for i in range(quantidade):
        numero = int(input("Digite um número:"))
        lista.append(numero)
    media = sum(lista) / quantidade
    return media

resultado = calculo_media()
print(f"Resultado: {resultado}")

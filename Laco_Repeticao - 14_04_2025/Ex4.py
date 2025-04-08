numero_minimo = int(input("Digite o primeiro número:"))
numero_maximo = int(input("Digite o segindo númeor:"))

for num in range(numero_minimo, numero_maximo + 1): #O num recebe os valores do intervalo
    if num >= 1:
        for i in range(2, num):
            if (num % i) ==0:
                break
        else:
            print(num)



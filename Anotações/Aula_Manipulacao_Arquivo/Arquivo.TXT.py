import csv

with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Olá mundo, eu sou Leticia Roth!\n")
    arquivo.write("Aprendendo Python!\n")


#Abre o arquivo em modo de leitura, "r"
arquivo = open("meu_arquivo.txt", "r")
#Lê o conteúdo do arquivo
resultado = arquivo.read()
print(f"Modo 1 \n{resultado}")
#reusltado = arquivo.readlines() - lê com tudo na linha


#Colocar caminho se não estiver dentro da pasta
with open("meu_arquivo.txt", "r") as arquivo:
    arquivo = open("meu_arquivo.txt", "r")
    conteudo = arquivo.read()
    print(f"Modo 2 \n{conteudo}")


#Outra maneira de printar
with open("meu_arquivo.txt", "r") as arquivo:
    print(f"Modo 3 \n{arquivo.read()}")































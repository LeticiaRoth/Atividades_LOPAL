taxa_reproducao = int(input("Digite a taxa de reprodução "))
taxa_mortalidade = int(input("Digite a taxa de mortalidade: "))
numero_inicial = int(input("Digite a quantidade inicial de coelhos: "))
geracoes = int(input("Digite as gerações: ")) #Recebo a quantidade de gerações que serão calculadas


for geracao in range(geracoes): ## Repete o cáculo, a variável geracao vai de 0 até geracoes - 
    numero_inicial = (numero_inicial * taxa_reproducao) - taxa_mortalidade
    
print(f" A quantidade de coelhos após {geracao} gerações é de {numero_inicial}")

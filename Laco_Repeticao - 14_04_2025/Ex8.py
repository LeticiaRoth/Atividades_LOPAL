import random

sequencia = []  #Cria uma sequencia com as jogadas
caras = 0  #Conta quantas vezes cara saiu seguidamente
tentativas = 0  #Guarda os resultados dos lançamentos da moeda

while caras < 3:  #Executa o código até er 3 caras seguidas
    resultado = random.choice (["cara", "coroa"])  #Escolhe aleaoriamente entre as duas opções
    sequencia.append(resultado)   #Guarda os resultados dentro da lista sequencia
    tentativas += 1   #A cada lançamento, soma 1 a variável tentativas
    
    if resultado == "cara":  #Se o resultado for cara, soma mais 1 ao contador
        caras += 1 
    else:
        caras = 0
        
print (f"Sequencia de jogadas")
print (sequencia)
print(f"Número de tentativas até sair 3 'caras' seguidas: {tentativas}")
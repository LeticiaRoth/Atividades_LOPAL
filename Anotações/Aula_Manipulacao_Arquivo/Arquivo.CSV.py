import csv #Importo a biblioteca CSV

dados_loja = [['Nome Livro', 'Autor(a)'],
              ['Assim que Acaba', 'Collen Hoover'],
              ['Dom Casmurro','Machado de Assis']]

#newline é usado para evitar linhas em branco adicionais no arquivo CSV
with open('dados_livraria.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile) #Crio o objeto escritor

    escritor.writerow(dados_loja[0])#Funciona por íncice, esccreve o cabeçalho

    escritor.writerows(dados_loja[1:])#Escreve o restante


"""
writerow(lista)  escreve uma linha de dados, onde a lista conté os valores
de cada linha

writerows(lista_de_listas) = funciona como o excel, temos uma linha com os valores
e outras com quais são, as sublistas, as colunas seriam ler o valores e suas atribuições

write(string) = escreve uma string diretamente no arquivo
"""
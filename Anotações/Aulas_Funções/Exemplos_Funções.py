"""

#Exemplo 1 - Chamar uma saudação
def saudacao():
    print("Olá mundo!")

saudacao()



#Exemplo 2 - Cálculo de média
#Definindo a função para calcular a media
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) /2
    return  media

#Pedindo ao usuário fora da função
nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a primeira nota:"))

#Chamando a função calcular média e aramazenando na variável resultado
resultado = calcular_media(nota1, nota2)

#Exbindo a média
print(f"Média entre as notas {nota1} e {nota2} é {resultado}")




#Exemplo 3 - Variável local
def minha_funcao():
    x = 14 #Variável local
    print(x)

minha_funcao()




#Exemplo 4 - Variável global
y = 20 #Apenas um exemplo, antes do def apenas biblioteca

def outra_funcao():
    print(y)

outra_funcao() #Posso usar ela aqui, sendo chamada
print(y) #Posso usar ela sendo printada




#Exemplo 5 - Variável global (alteração)
def mudar_valor():
    global z #Mudar valor da variável z
    z = 100

z = 5
mudar_valor()
print(z) #Agora z vale 100

def aumentar_contador():
    global contador
    contador += 1 #Altero o valor da variável

contador = 0 #Variável global
aumentar_contador()
print(contador)



#Exemplo 6 - Tentar mudar variável sem global
def mudar_variavel():
    a = 50 #Criou uma variável local, pois não coloquei o global
    print(a)

a = 7 #Variável global já definida
mudar_variavel() #Printa 50
print(a) #Printa 7


#Exemplo 7 - None
def diz_ola():
    print("Olá")


resultado = diz_ola()
print(resultado)
"""

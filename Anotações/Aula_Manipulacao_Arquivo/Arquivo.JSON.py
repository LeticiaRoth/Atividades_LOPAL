import json

dados ={
    "nome": "Leticia",
    "idade": 18,
    "cidade":"Hortolândia"
}

#Idento o arquivo e coloco no formmato UTF-8
with open("dados_pessoais.json","w", encoding="UTF-8") as arquivo:
    json.dump(dados,arquivo, indent=4, ensure_ascii=False)

print("Arquivo dados pessoais criado!")
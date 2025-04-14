import random 

# Lista corrigida
palavras = ["márcia", "python", "desenvolvimento", "sistemas", "tecnologia"]
palavra = random.choice(palavras).lower()  # Transforma tudo em minúsculo

letras_erradas = [] 
letras_certas = []
tentativas = 6

print("***** Bem-vindo ao Jogo da Forca *****")
print("_ " * len(palavra))  # Mostra o tamanho da palavra com espaços

while tentativas > 0:
    letra = input("\nDigite uma letra: ").lower()  # Transforma em minúsculo

    if letra in letras_erradas or letra in letras_certas: #Verifica se a letra está dentro de alguma das listas, e continua
        print("Você já digitou essa letra. Escolha outra.")
        continue

    if letra in palavra:
        letras_certas.append(letra)
        print("✅ Letra correta! Continue jogando.")
    else:
        letras_erradas.append(letra) #Se a letra estiver errada, diminui 1 das tentativas
        tentativas -= 1
        print(f"Letra errada! Restam {tentativas} tentativas.")

    progresso = ""
    for l in palavra:
        if l in letras_certas:
            progresso += l + " "
        else:
            progresso += "_ "

    print("\nPalavra:", progresso)
    print("Letras erradas:", ", ".join(letras_erradas)) #.join usado para separar itens numa lista, diferente do separar

    if all(l in letras_certas for l in palavra):
        print(f"\nParabéns, você ganhou! A palavra era: {palavra}")
        break

else:
    print("\nFim de jogo! Você perdeu.")
    print(f"A palavra era: {palavra}")

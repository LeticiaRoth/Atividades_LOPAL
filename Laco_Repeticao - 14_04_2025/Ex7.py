frase = str(input("Digite a frase desejada:"))
vogal_a = 0
vogal_e =0
vogal_i = 0
vogal_o = 0
vogal_u = 0

frase=frase.lower()

for vogal in frase:
    if vogal == 'a':
        vogal_a += 1

    elif vogal == 'e':
        vogal_e += 1

    elif vogal == 'i':
        vogal_i += 1

    elif vogal_o == 'o':
        vogal_o += 1

    elif vogal_u == 'u':
        vogal_u += 1

print(f"\nTotal de A {vogal_a}")
print(f"Total de E {vogal_e}")
print(f"Total de I {vogal_i}")
print(f"Total de O {vogal_o}")
print(f"Total de U {vogal_u}")

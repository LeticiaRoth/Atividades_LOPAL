import random

numero = random.randint(1, 10)
tent1 = int(input("Escolha um número: "))

if tent1 == numero:
    print("Parabéns! Você acertou na primeira tentativa!")

else:
    if tent1 < numero:
        print("O número é MAIOR")
    else:
        print("O número é MENOR")

    tent2 = int(input("Escolha outro número: "))

    if tent2 == numero:
        print("Você acertou na segunda chance!")
    else:
        print(f"Você perdeu, o número era {numero}")

horas = int (input("Digite a hora:"))
minutos = int (input("Digite os minutos:"))
segundos = int (input("Digite os segundos:"))


if horas >= 0 and horas < 24 and minutos >= 0 and minutos < 60 and segundos >= 0 and segundos < 60:
    print(f"Hora válida")

else:
    print(f"Hora inválida")
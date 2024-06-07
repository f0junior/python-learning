maior_peso = 0.0
menor_peso = 0.0
controle = "0.0"

while controle.replace(".", "", 1).isdigit():
    controle = input("Informe o peso da pessoa: ")
    if not controle.replace(".", "", 1).isdigit():
        continue

    peso = float(controle)
    if peso > maior_peso:
        maior_peso = peso

    if menor_peso == 0.0 or peso < menor_peso:
        menor_peso = peso

    print("Para finalizar digite qualquer LETRA.")

print("O MAIOR Peso lido foi de {:.1f} Kg".format(maior_peso))
print("O MENOR Peso lido foi de {:.1f} Kg".format(menor_peso))

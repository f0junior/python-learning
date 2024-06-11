valor_valido = False

while not valor_valido:
    sexo = input("Informe seu sexo: [M/F] ").strip().upper()
    valor_valido = sexo in "MF"

    if not valor_valido:
        print("Valor informado é inválido.\n")

print("Valor válido informado.")

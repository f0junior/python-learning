while True:
    ano = int(input("Informe o ano que seja verificar: "))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("O ano {} é bissexto.".format(ano))
        continue

    print("O ano {} não é bissexto.".format(ano))

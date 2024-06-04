while True:
    numero = int(input("Informe um número inteiro: "))

    numero_divisivel_menos_dois = numero % 2 == 0 and numero != 2
    numero_divisivel_menos_tres = numero % 3 == 0 and numero != 3
    numero_divisivel_menos_cinco = numero % 5 == 0 and numero != 5
    numero_divisivel_menos_sete = numero % 7 == 0 and numero != 7

    if numero < 2 or (
        numero_divisivel_menos_dois
        or numero_divisivel_menos_tres
        or numero_divisivel_menos_cinco
        or numero_divisivel_menos_sete
    ):
        print("{} não é um número primo.".format(numero))
        continue

    print("{} é primo.".format(numero))
1

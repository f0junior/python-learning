while True:
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        print("O número {} é par.".format(numero))
        continue
    print("O número {} é impar.".format(numero))

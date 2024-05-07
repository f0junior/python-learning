while True:
    numeros = [0, 0, 0]
    for index, value in enumerate(numeros):
        numeros[index] = int(input("Informe um numero: "))

    numeros.sort()
    print("Ö menor número é {} e o maior é {}".format(numeros[0], numeros[2]))

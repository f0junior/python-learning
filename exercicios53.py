while True:
    frase = input("Informe uma frase: ").strip()
    frase_sem_espaco = frase.replace(" ", "").upper()
    inverso = frase_sem_espaco[::-1]

    print("O inverso de {} é {}".format(frase_sem_espaco, inverso))

    if frase_sem_espaco == inverso:
        print("Temos um palíndromo")

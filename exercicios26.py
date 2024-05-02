while True:
    frase = input("Informe sua frase: ").strip()
    fraseUpper = frase.upper()
    print("A letra 'A' aparece {} vezes em sua frase.".format(fraseUpper.count("A")))
    print(
        "A primeira vez que a letra 'A' aparece é na posição {}.".format(
            fraseUpper.find("A") + 1
        )
    )
    print(
        "A última vez que a letra 'A' aparece é na posição {}.".format(
            fraseUpper.rfind("A") + 1
        )
    )

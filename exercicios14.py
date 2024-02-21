while True:
    celsius = float(input("Informe a temperatura em ˚C (celsius): "))

    print(
        "A temperatura de {:.1f}˚C corresponde a {:.1f}˚F".format(
            celsius, celsius * 1.8 + 32
        )
    )

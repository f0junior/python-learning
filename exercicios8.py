while True:
    metros = float(input("Informe valor em metros: "))
    print(
        "{} metro(s) tem {} centímetros e {} milímetros.".format(
            metros, metros * 100, metros * 1000
        )
    )

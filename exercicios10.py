while True:
    dinheiroEmReal = float(input("Informe valor em reais (exemplo: 5.89): "))
    cotacaoDolar = 3.27

    dinheiroEmDolar = dinheiroEmReal / cotacaoDolar
    print(
        "É possível comprar {:.2f} dolar com {} considerando a cotação do dolar de {}".format(
            dinheiroEmDolar, dinheiroEmReal, cotacaoDolar
        )
    )

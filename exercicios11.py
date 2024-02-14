while True:
    largura = float(input("Informe a largura da parede em metros: "))
    altura = float(input("Informe a altura da parede em metros: "))

    area = largura * altura

    print(
        "É necessário {:.2f} litro(s) de tinta para pintar uma parede de {:.2f} largura por {:.2f} de altura".format(
            area / 2, largura, altura
        )
    )

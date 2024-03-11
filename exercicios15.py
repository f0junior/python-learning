while True:
    dias = int(input("Quantos dias alugados: "))
    km = int(input("Quantos km rodados: "))

    print("O total a pagar é de R$ {:.2f}".format(dias * 60 + km * 0.15))

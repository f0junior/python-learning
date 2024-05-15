while True:
    notaUm = float(input("Informe sua primeira nota: "))
    notaDois = float(input("Informe sua segunda nota: "))

    media = (notaUm + notaDois) / 2
    if media < 5.0:
        print("Média {:.1f}: REPROVADO".format(media))
    elif media >= 7.0:
        print("Média {:.1f}: APROVADO".format(media))
    else:
        print("Média {:.1f}: RECUPERAÇÃO".format(media))

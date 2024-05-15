from datetime import date

while True:
    ano = int(input("Informe seu ano de nascimento (XXXX): "))

    idade = date.today().year - ano

    categoria = "MIRIM"

    if idade > 25:
        categoria = "MASTER"
    elif idade > 19:
        categoria = "SÊNIOR"
    elif idade > 14:
        categoria = "JÚNIOR"
    elif idade > 9:
        categoria = "INFANTIL"

    print(
        "De acordo com sua idade ({} anos) sua categoria é {}".format(idade, categoria)
    )

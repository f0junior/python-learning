from datetime import date

while True:
    ano = int(input("Informe seu ano de nascimento (XXXX): "))

    idade = date.today().year - ano

    if idade > 18:
        print("Já passou {} ano(s) para o alistamento militar.".format(idade - 18))
    elif idade < 18:
        print("Falta {} ano(s) para o alistamento militar.".format(18 - idade))
    else:
        print("Deve fazer seu alistamento militar esse ano.")

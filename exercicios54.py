from datetime import date

controle = "0"
pessoas = []

while controle.isdigit():
    controle = input("Informe a data de nascimento da pessoa: ")
    if not controle.isdigit():
        continue

    pessoas.append(int(controle))
    print("Para finalizar digite qualquer LETRA.")

maior_idade = 0
menor_idade = 0
ano_atual = date.today().year

for pessoa in pessoas:
    if ano_atual - pessoa < 18:
        menor_idade += 1
        continue

    maior_idade += 1

print("Ao todo temos {} pessoa(s) maior(es) de idade.".format(maior_idade))
print("E também temos {} pessoa(s) menor(es) de idade.".format(menor_idade))

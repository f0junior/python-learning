idades = []
num_mulheres_menos_vinte = 0
homem_mais_velho = dict(nome="", idade=0)

nome = "teste"
while len(nome) > 0:
    nome = input("Informe o nome da pessoa: ").strip()
    if len(nome) == 0:
        continue

    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo [M/ F]: ").strip().upper()

    idades.append(idade)
    if sexo == "M" and homem_mais_velho["idade"] < idade:
        homem_mais_velho["nome"] = nome
        homem_mais_velho["idade"] = idade
    elif sexo == "F" and idade < 20:
        num_mulheres_menos_vinte += 1

    print("Para finalizar pressione ENTER sem digitar qualquer valor.\n")

print("\nA média de idade do grupo é de {:.1f} anos.".format(sum(idades) / len(idades)))
print(
    "O homem mais velho tem {} anos e se chama {}.".format(
        homem_mais_velho["idade"], homem_mais_velho["nome"]
    )
)
print("Ao todo são {} mulheres com menos de 20 anos.".format(num_mulheres_menos_vinte))

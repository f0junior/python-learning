pessoas = []

while True:
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo: [M/F] ").strip().upper()

    pessoas.append({"idade": idade, "sexo": sexo})

    continuar = input("Dseja continuar: [S/N] ").strip().upper()
    if continuar == "N":
        break

maior_idade = homens = mulher_menor_vinte = 0
for pessoa in pesssoas:
    if pessoa.idade > 18:
        maior_idade += 1
    
    if pessoa.sexo == 'M':
        homens += 1
    elif pessoa.idade < 20:
        mulher_menor_vinte += 1

print(f"{maior_idade} pessoas tem mais de 18 anos.")
print(f"{homens} homens cadastrados.")
print(f"{mulher_menor_vinte} mulheres com menos de 20 anos.")

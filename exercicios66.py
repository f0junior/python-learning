soma = qtd = 0

while True:
    numero = int(input("Informe um número inteiro: "))
    if numero == 999:
        break

    soma += numero
    qtd += 1

print(f"Foram informados {qtd} números e a soma deles é igual a {soma}")

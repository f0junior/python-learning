numero = count = soma = 0

while numero != 999:
    numero = int(input("Informe um número inteiro: [999 para finalizar]"))
    if numero == 999:
        continue

    count += 1
    soma += numero

print("~" * 47)
print("Foram informados {} números e a soma deles é {}.".format(count, soma))

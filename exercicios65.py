controle = "S"
maior = menor = count = soma = 0

while controle in "Ss":
    numero = int(input("Digite um número inteiro: "))
    count += 1
    soma += numero

    if numero > maior:
        maior = numero

    if menor == 0.0 or numero < menor:
        menor = numero

    controle = input("Deseja continuar? [S/N] ").upper().strip()[0]

print("~" * 47)
print("Você digitou {} número(s) e a média foi {:.2f}".format(count, soma / count))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
print("~" * 47)

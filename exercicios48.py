print(
    "Soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500"
)

soma = 0
for i in range(3, 501, 2):
    if i % 3 == 0:
        soma += i

print("Resultado é {}.".format(soma))

from math import factorial

while True:
    numero = int(input("Informe um número: "))

    # numb = numero
    # result = 1
    # while numb > 0:
    #     result = result * numb
    #     numb -= 1
    result = factorial(numero)
    print("Fatorial de {} é {}.\n".format(numero, result))

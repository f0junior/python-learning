from math import trunc

while True:
    numero = float(input("Digite um número com ponto flutuante: "))

    print("A porção inteira do número {} é {}".format(numero, trunc(numero)))

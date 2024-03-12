from math import hypot

while True:
    catetoO = float(input("Informe o cateto oposto: "))
    catetoA = float(input("Informe o cateto adjacente: "))

    print("O comprimento da hipotenusa é {:.2f}".format(hypot(catetoO, catetoA)))

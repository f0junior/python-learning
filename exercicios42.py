while True:
    r1 = float(input("Informe a primeira reta: "))
    r2 = float(input("Informe a segunda reta: "))
    r3 = float(input("Informe a terceira reta: "))

    if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
        print("É possível formar um triângulo com os valores informados.", end="")

        if r1 == r2 == r3:
            print("Do tipo EQUILÁTERO.")
        elif r1 != r2 != r3 != r1:
            print("Do tipo ESCALENO.")
        else:
            print("Do tipo ISÓSCELES.")

        continue
    print("Não é possível formar um triângulo com os valores informados.")

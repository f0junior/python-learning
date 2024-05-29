while True:
    primeiroTermo = int(input("Informe o primeiro termo: "))
    razao = int(input("Informe a razão: "))

    for i in range(10):
        print("{} -> ".format(primeiroTermo), end="")
        primeiroTermo += razao

    print("Acabou.")

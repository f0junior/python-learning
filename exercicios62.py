primeiroTermo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))

termos = 10
termos_mostrados = termos
while termos > 0:
    for i in range(termos):
        print("{} -> ".format(primeiroTermo), end="")
        primeiroTermo += razao

    print("Pausa")
    termos = int(input("Quantos termos você quer mostrar a mais? "))
    termos_mostrados += termos
print("\nProgressão finalizada com {} termos mostrados.".format(termos_mostrados))
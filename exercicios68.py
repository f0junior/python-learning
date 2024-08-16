import random

print("Vamos jogar Impar ou Par")

vitorias = 0
while True:
    aleatorio = random.randint(1, 10)

    numero = int(input("Escolha um valor: "))
    impar_ou_par = input("Impar ou par? [I/P]").strip().upper()

    soma = aleatorio + numero

    print(f"Você jogou {numero} e o computador jogou {aleatorio}.")
    print(f"Total igual a {soma}, deu ", end="")
    result = "Par" if soma % 2 == 0 else "Impar"
    print(f"{result}.")

    if (soma % 2 == 0 and impar_ou_par == "P") or (
        soma % 2 != 0 and impar_ou_par == "I"
    ):
        vitorias += 1
        print("Você ganhou, vamos mais uma.")
    else:
        print("Você perdeu.")
        print(f"Game Over! Você ganhou {vitorias} vezes.")
        break

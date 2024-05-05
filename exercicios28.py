from random import randint

numero = randint(0, 5)
chute = 6

while chute != numero:
    chute = int(input("Adivinhe o número que pensei (1 a 5): "))

    if chute == numero:
        print("Acertou mizeravi.")
    else:
        print("Tente novamente.")

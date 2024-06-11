from random import randint

numero = randint(1, 10)
chute = -1
numb_chutes = 0

while chute != numero:
    chute = int(input("Adivinhe o número que pensei (1 a 10): "))
    numb_chutes += 1

    if chute == numero:
        print("Acertou mizeravi.")
    elif chute > numero:
        print("Errou, o número é menor.")
    else:
        print("Errou, o número é maior.")

print("\nForam necessários {} chute(s).".format(numb_chutes))

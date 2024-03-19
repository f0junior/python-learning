import math

while True:
    angulo = float(input('Informe o ângulo que você deseja: '))
    rad = math.radians(angulo)

    print("O ângulo de {:.1f} tem o Seno de {:.2f}".format(angulo, math.sin(rad)))
    print("O ângulo de {:.1f} tem o Cosseno de {:.2f}".format(angulo, math.cos(rad)))
    print("O ângulo de {:.1f} tem o Tangente de {:.2f}".format(angulo, math.tan(rad)))
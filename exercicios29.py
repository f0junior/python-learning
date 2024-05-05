limite = 80

while True:
    velocidade = int(input("Qual é a velocidade atual do seu carro? "))
    if velocidade > limite:
        print("Você excedeu o limite de velocidade que é 80 Km/h.")
        print("Sua multa é de R$ {:.2f}.".format((velocidade - limite) * 7))

    print("Tenha um bom dia! Dirija com cuidado!")

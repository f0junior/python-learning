while True:
    distViagem = int(input("Informe a distância da viagem em km: "))
    custo = 0.5
    if distViagem > 200:
        custo = 0.45

    print("O custo para a viagem é de R${:.2f}".format(distViagem*custo))
while True:
    produto = float(input("Informe valor do produto: "))
    print("Formas de pagamento:")
    print("[1] à vista dinheiro/cheque")
    print("[2] à vista no cartão")
    print("[3] 2x no cartão")
    print("[4] 3x ou mais no cartão")
    formaPagamemto = int(input("Informe a forma de pagamento: "))

    match (formaPagamemto):
        case 1:
            total = produto * 0.9
        case 2:
            total = produto * 0.95
        case 3:
            total = produto
            parcela = total / 2
            print("Sua compra vai ser parcelada em {}X de R$ {:.2f}".format(2, parcela))
        case 4:
            total = produto * 1.2
            totparc = int(input("Número de parcelas: "))
            parcela = total / totparc
            print(
                "Sua compra vai ser parcelada em {}X de R$ {:.2f}".format(
                    totparc, parcela
                )
            )
        case _:
            print("Opção inválida.")
            continue

    print(
        "Sua compra de R$ {:.2f}, vai ficar R$ {:.2f} no final.".format(produto, total)
    )

while True:
    valorProduto = float(input("Informe o preço do produto: "))

    print(
        "O produto no valor de R$ {:.2f} vai ficar por R$ {:.2f} com 5% de desconto".format(
            valorProduto, valorProduto * 0.95
        )
    )

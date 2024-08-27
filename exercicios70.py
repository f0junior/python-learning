compra = []

while True:
    produto = input("Informe o nome do produto: ")
    valor = float(input(f"Informe o preço do(a) {produto}: "))

    compra.append({"nome": produto, "valor": valor})

    continuar = input("Dseja continuar: [S/N] ").strip().upper()
    if continuar == "N":
        break

valorTotal = maior_mil = mais_barato = 0
for produto in compra:
    valorTotal += produto["valor"]

    if produto["valor"] > 1000.0:
        maior_mil += 1

    if mais_barato == 0 or mais_barato["valor"] > produto["valor"]:
        mais_barato = produto

print(f"Valor total da compra é R$ {valorTotal}.")
print(f"{maior_mil} produto(s) tem preço superior a R$ 1000.00")
print(f"O produto mais barato é {mais_barato['nome']}.")

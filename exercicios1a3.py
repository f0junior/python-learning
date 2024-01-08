nome = input("Olá, Com quem estou falando: ")
print("É um prazer conhecê-lo", nome)

dia = input("Por gentileza, informe seu dia de nascimento: ")
mes = input("Agora preciso que informe o mês: ")
ano = input("Por último o ano: ")

print("{}/{}/{} sua data de nascimento formatada.".format(dia, mes, ano))

print("Por último iremos fazer uma conta de soma.")
primeiroNumero = int(input("Por gentileza, informe um número: "))
segundoNumero = int(input("Agora outro número: "))

print(
    "A soma entre {} e {} vale {}.".format(
        primeiroNumero, segundoNumero, primeiroNumero + segundoNumero
    )
)

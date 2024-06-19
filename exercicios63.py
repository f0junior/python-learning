primeiro_termo = 0
segundo_termo = 1

n = int(input("Quantos termos você quer mostrar? "))
print("~" * 47)
print("{} -> {} -> ".format(primeiro_termo, segundo_termo), end="")

for x in range(n-2):
    novo_termo = primeiro_termo + segundo_termo
    print("{} -> ".format(novo_termo), end="")
    primeiro_termo = segundo_termo
    segundo_termo = novo_termo

print("FIM")
print("~" * 47)

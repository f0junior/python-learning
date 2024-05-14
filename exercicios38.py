while True:
    f_numb = int(input("Informe o primeiro número: "))
    s_numb = int(input("Informe o segundo número: "))

    if f_numb > s_numb:
        print("O primeiro valor é maior.")
    elif s_numb > f_numb:
        print("O segundo valor é maior.")
    else:
        print("Não existe valor maior, os dois são iguais.")

from random import shuffle

while True:
    alunos = []

    while len(alunos) < 4:
        alunos.append(input("Informe o nome do aluno: "))

    print("A ordem de apresentação será")
    shuffle(alunos)
    print(*alunos, sep=", ")
    print("\n")

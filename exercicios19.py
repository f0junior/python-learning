from random import choice

while True:
    alunos = []

    while len(alunos) < 4:
        alunos.append(input("Informe o nome do aluno: "))

    print("O aluno responsável por apagar o quadro é o(a) {}.\n".format(choice(alunos)))

while True:
    cidade = input("Informe o nome da cidade: ").strip()
    if cidade.upper().find("SANTO") == 0:
        print("Nome da cidade começa com Santo.")
    else:
        print("Nome da cidadde não começa com Santo.")

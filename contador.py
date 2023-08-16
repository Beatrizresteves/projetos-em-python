texto = input("Informe um texto: ")
palavras = texto.split()
qtd_palavras = len(palavras)


if qtd_palavras > 150:
    print(
        f"A quantidade de palavras no seu texto é {qtd_palavras}. Portanto, você ultrapassou a quantidade de palavras.")
else:
    print(
        f"A quantidade de palavras no seu texto é {qtd_palavras}. Portanto, você está dentro das regras da ABNT.")

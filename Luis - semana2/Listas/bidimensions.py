campo_naval = []

# Linhas (de 1 a 10)
for linha in range(1, 11):
    linha_naval = []

    # Colunas (de A a J)
    for coluna in range(ord('A'), ord('J') + 1):
        letra_coluna = chr(coluna)
        celula = f"{letra_coluna}{linha}"
        linha_naval.append(celula)

    campo_naval.append(linha_naval)

# Campo de batalha naval
for linha in campo_naval:
    print(linha)


print(f"A primeira linha do campo: {campo_naval[0]}")
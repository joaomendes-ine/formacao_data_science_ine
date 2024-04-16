from modulos import conversor

metros_em_milhas = float(input("Insira um valor para calcular a distância em milhar: "))
nr_colheres = int(input("Insira o número de colheres: "))

print(f"A distância em milhas: {conversor.metros_em_milhas(metros_em_milhas):.2}")
print(f"{nr_colheres} número de colheres equivale a: {conversor.colher_de_manteiga_em_gramas(nr_colheres)}")

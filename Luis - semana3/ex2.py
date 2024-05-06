def get_comuns(l1, l2, l3):
    # Listas em conjuntos
    set1 = set(l1)
    set2 = set(l2)
    set3 = set(l3)
    
    # Interseção de todos os conjuntos
    comuns = set1.intersection(set2, set3)
    
    return list(comuns)

#BONUS
def get_comuns_poly(*args):
    sets = [set(lst) for lst in args]
    
    comuns = set.intersection(*sets)
    
    return list(comuns)

# Teste
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
lista3 = [5, 6, 7, 8, 9]

resultado1 = get_comuns(lista1, lista2, lista3)
resultado2 = get_comuns_poly(lista1, lista2)

print(resultado1, resultado2)
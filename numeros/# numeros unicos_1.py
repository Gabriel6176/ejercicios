# numeros unicos

numeros = [1, 2, 2, 3, 3, 4, 5]


def obten_numeros_unicos(numeros):

    lista_de_numeros_unicos = []

    numeros_unicos = set(numeros)

    for numero in numeros_unicos:
        lista_de_numeros_unicos.append(numero)

    return lista_de_numeros_unicos


print(obten_numeros_unicos(numeros))
# resultado: [1, 2, 3, 4, 5]


# numeros unicos_4
#el resultado no aparece ordenado sino que a medida queva iterando va agregando a la lista que comienza vacia

numeros = [20, 50, 50, 20, 30, 30, 40]


def obten_numeros_unicos(numeros):
    unicos = []

    for numero in numeros:
        if numero in unicos:
            continue
        else:
            unicos.append(numero)
    return unicos


print(obten_numeros_unicos(numeros))
# Resultado: [20, 50, 30, 40]
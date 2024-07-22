## funciones

def mi_funcion(num1, num2):
    print(num1+num2)
mi_funcion(3, 4)

# *algo es una tupla
def mi_funcion(cad, v=2, *algo):
    print(cad * v)
    for cadena in algo:
        z = 3
        print(cadena * z)
        
mi_funcion("Hola", 5, "hola", "Como", "Estas")

# si pongo **algo eso sera un diccionario

# cuenta de palabras
"""Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que quiera que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))

# respuesta: {'Como': 1, 'quieres': 1, 'que': 4, 'quiera': 3, 'quiero': 2, 'me': 3, 'no': 1, 'quiere': 1}




  
    


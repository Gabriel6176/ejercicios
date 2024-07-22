#199 leer archivo en bytes
from urllib.request import Request
from urllib.request import urlopen

url2= Request ('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
url2.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
url2.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')

url='http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
url=url2


with urlopen(url) as mensaje:
    contenido = mensaje.read()
    print(contenido)

#nos devuelve: b'contenido xx'

#--------------------------

with urlopen(url) as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)
#nos devuelve: xx

#guardar informacion en archivo txt
with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(contenido)


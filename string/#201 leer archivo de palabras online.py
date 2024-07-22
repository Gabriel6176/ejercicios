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


#contar ocurrencias de una cadena
print(contenido.count(b'Universidad'))
#nos devuelve el numero de veces ejemplo 7

#metodo upper - convierte a upper el contenido
print(contenido.upper())
#retorna todo el texto en mayusculas

#metodo lower - convierte a lower el contenido
print(contenido.lower())
#retorna todo el texto en minusculas

#buscar si esta la palabra python en el contenido
print(b'python'.lower() in contenido.lower())
#devuelve valor True si existe ya que tanto el texto escrito como el contenido se convirtio a lower

#inicia con o finaliza con
print(contenido.startswith(b'En GlobalMentoring.com.mx'))
#devuelve valor True

print(contenido.endswith(b'GlobalMentoring.com.mx'))
#devuelve valor True

#otra opcion donde primero convierto todo a lower case para que no enga error por ese lado
print(contenido.lower().endswith(b'GlobalMentoring.com.mx'.lower()))
#devuelve valor True

#preguntar si contiene en minusculas
mensaje= b'Hola Mundo'
print(mensaje.islower())
#retorna False
print(mensaje.lower().islower())
#retorna True porque previamente pase todo a lower




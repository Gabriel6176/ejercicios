from urllib.request import Request
from urllib.request import urlopen

url = Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
url.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
url.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
 
 
with urlopen(url) as mensaje:
    contenido=mensaje.read().decode('utf-8')
    print(contenido)


#201 leer archivo de palabras online
from urllib.request import Request
import urllib.request

url2= Request ('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
url2.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
url2.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')

url='http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
url=url2

with urllib.request.urlopen(url) as response:
   html = response.read()
   print(html)


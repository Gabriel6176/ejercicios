#scanear puertos
import nmap as nmap

ip=input('Que ip queres escanear: ')
nm = nmap.PortScanner()
results=nm.scan(ip)
print(results)



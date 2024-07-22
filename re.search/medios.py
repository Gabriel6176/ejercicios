#encoding=latin-1

import os
import re
import linecache


APP_PATH = os.getcwd()

#cuit2=20002545080

#cuit2=20000188299
#cuit2=20041522098
#cuit2=20273742558
#cuit2=20929969422
#cuit2=27115290016
#cuit2=27209836292
#cuit2=27602708123
#cuit2=30711231621
cuit2=30716597802
#cuit2=34686233482
#cuit2=34688333360
#cuit2=34999032089

#no esta en la lista
#cuit2=34999032088
#cuit2=20273742559
#cuit2=27115290017
#cuit2=34686233483
#cuit2=34999032090



with open(APP_PATH+'\\ARD1.txt', 'rb') as f:
    x = len(f.readlines())
    print(f'Total lineas: {x}')

linea=1
value=True

def print_resultado(linea, cuit, value):
    print(f'El resultado es: {linea} el cuit es: {cuit} y el value es: {value}')

def busqueda1(linea, value):
    count=1
    value=value
    while True:
        line=linecache.getline(APP_PATH+'\\ARD1.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'0 {resultado}')
        if count<50:
            if resultado == 0:
                print(f'es la linea: {linea}')
                print('encontrado')
                print_resultado(linea, cuit2, value)
                break
            elif resultado<-13000000000:
                print(f'1 {resultado}')
                if linea+449 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+449   
                    print('ok')
            elif resultado<-1300000000:
                print(f'2 {resultado}')
                if linea+129 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+129   
                    print('ok')
            elif resultado<-130000000:
                print(f'3 {resultado}')
                if linea+99 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+99   
                    print('ok')
            elif resultado<-13000000:
                print(f'4 {resultado}')
                if linea+17 > x:
                    linea=x-linea+linea
                    print(f'{linea}')
                else:
                    linea=linea+17   
                    print('ok')
            elif resultado<-1300000:
                print(f'5 {resultado}')
                if linea+7 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+7   
                    print('ok')
            elif resultado<-130000:
                print(f'6 {resultado}')
                if linea+3 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+3   
                    print('ok')
            elif resultado<-13000:
                print(f'7 {resultado}')
                if linea+3 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+3   
                    print('ok')
            elif resultado<-1300:
                print(f'8 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print('ok')
            elif resultado<-130:
                print(f'9 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print('ok')
            elif resultado<-13:
                print(f'10 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print('ok')
            elif resultado<13:
                print(f'11 {resultado}')
                if linea-1 <= 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<130:
                print(f'12 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<1300:
                print(f'13 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<13000:
                print(f'14 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<130000:
                print(f'15 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1  
                    print('ok')
                    count+=1
            elif resultado<1300000:
                print(f'16 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<13000000:
                print(f'17 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1
                    print('ok')
                    count+=1
            elif resultado<130000000:
                print(f'18 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<1300000000:
                print(f'19 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
        else:
            value=False
            print('No encontrado')
            linea=0
            print_resultado(linea, cuit2, value)
            break

def busqueda(linea, value):
    value=value
    count=1
    while True:
        line=linecache.getline(APP_PATH+'\\ARD1.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'0 {resultado}')
        if count<50:
            if resultado == 0:
                print(f'es la linea: {linea}')
                print('encontrado')
                print_resultado(linea, cuit2, value)
                break
            elif resultado<-13000000000:
                print(f'1 {resultado}')
                if linea+24989 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+24989   
                    print('ok')
            elif resultado<-1300000000:
                print(f'2 {resultado}')
                if linea+20089 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+20089   
                    print('ok')
            elif resultado<-130000000:
                print(f'3 {resultado}')
                if linea+15049 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+15049   
                    print('ok')
            elif resultado<-13000000:
                print(f'4 {resultado}')
                if linea+1029 > x:
                    linea=x-linea+linea
                    print(f'{linea}')
                else:
                    linea=linea+1029   
                    print('ok')
            elif resultado<-1300000:
                print(f'5 {resultado}')
                if linea+109 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+109   
                    print('ok')
            elif resultado<-130000:
                print(f'6 {resultado}')
                if linea+55 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+55   
                    print('ok')
            elif resultado<-13000:
                print(f'7 {resultado}')
                if linea+25 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+25   
                    print('ok')
            elif resultado<-1300:
                print(f'8 {resultado}')
                if linea+15 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+15   
                    print('ok')
            elif resultado<-130:
                print(f'9 {resultado}')
                if linea+5 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+5   
                    print('ok')
            elif resultado<-13:
                print(f'10 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print('ok')
            elif resultado<13:
                print(f'11 {resultado}')
                if linea-1 <= 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print('ok')
                    count+=1
            elif resultado<130:
                print(f'12 {resultado}')
                if linea-2 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-2   
                    print('ok')
                    count+=1
            elif resultado<1300:
                print(f'13 {resultado}')
                if linea-6 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-6   
                    print('ok')
                    count+=1
            elif resultado<13000:
                print(f'14 {resultado}')
                if linea-56 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-56   
                    print('ok')
                    count+=1
            elif resultado<130000:
                print(f'15 {resultado}')
                if linea-156 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-156  
                    print('ok')
                    count+=1
            elif resultado<1300000:
                print(f'16 {resultado}')
                if linea-556 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-556   
                    print('ok')
                    count+=1
            elif resultado<13000000:
                print(f'17 {resultado}')
                if linea-1056 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1056
                    print('ok')
                    count+=1
            elif resultado<130000000:
                print(f'18 {resultado}')
                if linea-4056 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-4056   
                    print('ok')
                    count+=1
            elif resultado<1300000000:
                print(f'19 {resultado}')
                if linea-10046 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-10046   
                    print('ok')
                    count+=1
        else:
            value=False
            print('no encontrado')
            linea=0
            print_resultado(linea, cuit2, value)
            break

if __name__=="__main__":
    value=True
    if cuit2>34000000000:
        busqueda1(linea, value)
    else:
        busqueda(linea, value)







'''
def capa1(resultado, linea):
    if resultado<-30000000:
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'1 {resultado}')
        #capa1(resultado, int(linea+100000))
        print(resultado, int(linea+100000))
    elif resultado<-25000000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'2 {resultado}')
        #capa1(resultado, int(linea+750000))
        print(resultado, int(linea+750000))
    elif resultado<-20000000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'3 {resultado}')
        #capa1(resultado, int(linea+500000))
        print(resultado, int(linea+750000))
    elif resultado<-15000000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'4 {resultado}')
        #capa1(resultado, int(linea+300000))
        print(resultado, int(linea+750000))
    elif resultado<-10000000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'5 {resultado}')
        #capa1(resultado, int(linea+150000))
        print(resultado, int(linea+750000))
    elif resultado<-5000000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'6 {resultado}')
        #capa1(resultado, int(linea+150000))
        print(resultado, int(linea+750000))
    elif resultado<-3000000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'7 {resultado}')
        #capa1(resultado, int(linea+100000))
        print(resultado, int(linea+750000))   
    elif resultado>-1500000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'8 {resultado}')
        print((linea))
        print(linea+75000)
        resultado=0
        capa1(resultado, linea)
        print(resultado, int(linea+750000))
    elif resultado>-750000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'9 {resultado}')
        capa1(resultado, int(linea+50000))
    elif resultado>-350000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'10 {resultado}')
        capa1(resultado, int(linea+50000))
    elif resultado>-150000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'11 {resultado}')
        capa1(resultado, int(linea+10000))
    elif resultado>-75000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'12 {resultado}')
        capa1(resultado, int(linea+7500))
    elif resultado>-30000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'13 {resultado}')
        capa1(resultado, int(linea+5000))
    elif resultado>-15000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'14 {resultado}')
        capa1(resultado, int(linea+3000))
    elif resultado>-7000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'15 {resultado}')
        capa1(resultado, int(linea+500))
    elif resultado>-3500:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'16 {resultado}')
        capa1(resultado, int(linea+100))
    elif resultado>-1500:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'17 {resultado}')
        capa1(resultado, int(linea+50))
    elif resultado>-750:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'18 {resultado}')
        capa1(resultado, int(linea+30))
    elif resultado>-300:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'19 {resultado}')
        capa1(resultado, int(linea+10))
    elif resultado>-150:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'20 {resultado}')
        capa1(resultado, int(linea+5))
    elif resultado>-75:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'21 {resultado}')



def capa2(resultado, linea):
    if resultado>-1400000:
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(resultado)
    elif resultado>-1300000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(resultado)
    elif resultado>-1300000:    
        line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(resultado)
'''






'''
contador=1
incremento=100
exito=[]
conteo=1

def testeo_positivo(linea, conteo):
    line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
    texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
    resultado=int(texto)-int(cuit2)
    try:    
        if resultado == 0:
            print(f'{resultado}')
        elif resultado<0:
            testeo_positivo((linea+incremento))
            conteo+=1
        else:
            testeo_negativo((linea-(int(incremento/2))))
            conteo+=1
    except Exception as e:
        print(e)

def testeo_negativo(linea, conteo):
    line=linecache.getline(APP_PATH+'\\ARD3.txt', linea)
    texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
    resultado=int(texto)-int(cuit2)
    if resultado==0:
        print(f'{resultado}')
    elif resultado>0:    
        testeo_negativo((linea-(int(incremento/2))))
        conteo+=1
    else:
        testeo_positivo((linea+(int(incremento/2))))
        conteo+=1

if __name__ == "__main__":
    testeo_positivo(1, 1)
    '''
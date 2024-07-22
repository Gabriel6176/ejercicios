import calendar #Cal001

def ingreso():
   dia_semana = {0:"Lun", 1:"Mar", 2:"Mié", 3:"Jue", 4:"Vie", 5:"Sáb", 6:"Dom"}
   meses = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",
            8:"Agosto", 9:"Septiembre",10:"Octubre" ,11:"Noviembre",12:"Diciembre"}

   while True:
       while True:
           try:
               mes  = int(input("\n Ingrese més [1-12]...:"))
           except:
               print("\n El més ingresado es incorrecto...")
           else:
               if mes >= 1 and mes <= 12:
                   break

       while True:
           try:
               anio  = int(input("\n Ingrese año..........:"))
               break
           except:
               print("\n El año ingresado es incorrecto...")

       nom_dia_semana = dia_semana[calendar.weekday(anio, mes, 1)] #Cal002 

       for key in dia_semana: #Cal003 
           if dia_semana[key] == nom_dia_semana:
               num_dia_semana = key

       mostrar( mes, meses, anio, num_dia_semana )

       opc = input("\n ¿Desea hacer otra consulta? Si/No...: ")
       if opc != 'Si':
           break


def mostrar( mes, meses, anio, num_dia_semana ):
   dias_mes = tot_dias_mes( mes, anio ) #Cal004
   print()
   print("=" * 34)
   print(f"          {meses[mes]} {anio}")
   print("\n Dom  Lun  Mar  Mié  Jue  Vie  Sáb")
   dia = 0
   dias_mes = dias_mes + num_dia_semana #Cal005
   for a in range( dias_mes + 1 ):
       if a <= num_dia_semana: #Cal006
           print("     ", end="")
       else:
           dia += 1
           if a % 7 == 0: #Cal007
               print()
           if dia < 10:
               print(f"  0{dia}", end=" ") 
           else:
               print(f"  {dia}", end=" ")

   print()
   print("=" * 34)


def tot_dias_mes( mes, anio ):
   if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
       return 31
   if mes == 2:   
       if anio%4 == 0 and anio%100 != 0 or anio%400 == 0:
       return 29
   else:
       return 28
   if mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
       return 30

ingreso()

"""
================================ Ayuda ================================

Cal001: El módulo lo utilizamos para establecer el día de la semana
       (nombre) Lun, Mar, mié....
Cal002: Llamamos al diccionario "día_semana" y grabamos en la variable
       "nom_dia_semana" el nombre del día de la semana según los parametros
       de fechas pasados (anio, mes, 1) el uno es porque necesitamos
       Ubicar el día 1 en el correspondiente día (Lun, Mar, mié). -
Cal003: Con este bucle conseguimos el número del día de la semana 0,1,3
       4,5,6.-
Cal004: Llamamos a la función "tot_dias_mes" para establecer el total de
       días que tiene el mes pasado como parámetro(28/29 - 30 ó 31)
Cal005 dias_mes + num_dia_semana le sumamos a los días que tiene el mes
      (28/29 - 30 ó 31) el número correspondiente al número de la
      semana (0-1-2-3-4-5-6) de esta manera el bucle funciona perfecto. 
Cal006 "if a <= num_dia_semana:" mientra que el contador a sea menor o
      igual a "num_dia_semana" no se imprime ningún número solo espacios.-
Cal007 Cada vez que "a" sea divisible por 7 se produce un salto de línea.-
=======================================================================
"""
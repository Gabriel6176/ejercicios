#importar csv o txt lento

def importar(df, cuit, con, cursor):
    APP_PATH = os.getcwd()
    filename = APP_PATH+'\\'+df+'_2.txt'
    with open(filename, 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    linea=1
    while True:
        if linea<=x:
            line=linecache.getline(filename, linea)
            cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
            num_linea=re.search(';(.*)', line).group(1)
            con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
            cursor=con.cursor()
            #si es texto el dato le pongo comillas por fuera de '{nombre}'
            instruccion=f"INSERT INTO base VALUES({cuit},'{num_linea}');"
            cursor.execute(instruccion)
            con.commit()
            linea+=1
        else:
            print(' paso importar _va_ buscar cuit')
            return buscar_cuit(df, cuit)    



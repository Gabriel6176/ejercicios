import os
import re
import cchardet as chardet
import csv
import linecache

APP_PATH=os.getcwd()


dir_file=APP_PATH+'\\ard2.txt'

def detectar_si_utf():
    with open(dir_file, 'rb') as f:
        msg=f.read()
        detection=chardet.detect(msg)
        with open('procesado.txt', 'w') as r:
            r.write(str(detection))
        with open('procesado.txt', 'rb') as r:    
            line=linecache.getline(APP_PATH+'\\procesado.txt', 1)
            texto=re.search("ng': '(.+?)', 'con", line).group(1)
            if texto != 'UTF-8':
                #deberia convertir txt a UTF-8
                print('1')
            else:
                #deberia ir a la consulta sin convertir la base
                print('0')    
                
if __name__=='__main__':
    detectar_si_utf()
        
        

#name=b"\x4a\x6f\x73\x39"



'''
def read_content(dir_file):
    """ 
    Read the file as bite
    and return the content
    
    Arguments:
        dir_file {[str]} -- [description]
    
    Returns:
        [str] -- [description]
    """

    with open(dir_file,"rb") as rb:
        content = rb.read()
    
    encoder_code = chardet.detect(content)["encoding"]
    try:
        content = content.decode(encoder_code)
        print('hola')
    except:
        message = "This file code {} is error, and ignored".format(dir_file)
        print(message)
        content = content.decode(encoder_code, "ignore")
    return content 

if __name__=='__main':
    read_content(dir_file)    
'''
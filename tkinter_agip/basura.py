import os

APP_PATH=os.getcwd()
print(APP_PATH)
#--------------
#with open(APP_PATH+'\\procesado.txt', 'w') as f:
#    f.write(str(1)+'\n')
#    f.close()
#----------------------
encode='latin-1'

def inicio():
    try:
        with open(APP_PATH+'\\procesado.txt', 'r') as f:
            x = len(f.readlines())
            if x>0:
                pass
            else:
                print('else')
                df = 'ard'
                file_name=df+'.txt'
                dummy_file = file_name + '.bak'
                # open original file in read mode and dummy file in write mode
                with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as read_origin_file, open(dummy_file, 'w', encoding='utf-8') as write_obj:
                    for line in read_origin_file:
                        write_obj.write(line)
                        #print('procesando')
                # remove original file
                os.remove(file_name)
                # Rename dummy file as the original file
                os.rename(dummy_file, file_name)
                with open(APP_PATH+'\\procesado.txt', 'a') as f:
                    f.write(str(1)+'\n')    
    except:
        df = 'ard'
        file_name=df+'.txt'
        dummy_file = file_name + '.bak'
        # open original file in read mode and dummy file in write mode
        with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as read_origin_file, open(dummy_file, 'w', encoding='utf-8') as write_obj:
            for line in read_origin_file:
                write_obj.write(line)
                #print('procesando')
        # remove original file
        os.remove(file_name)
        # Rename dummy file as the original file
        os.rename(dummy_file, file_name)
        with open(APP_PATH+'\\procesado.txt', 'a') as f:
            f.write(str(1)+'\n')

if __name__=='__main__':
    inicio()
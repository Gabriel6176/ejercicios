import os


def confirm_db_exist():
    d1='archivo'
    archivo=d1+'.db'
    APP_PATH=os.getcwd()
    FILE_PATH=APP_PATH+'\\'+archivo

    resultado=os.path.exists(FILE_PATH)
    print(resultado)
    if resultado == True: 
        print('1')
    else:
        print('2')

if __name__=='__main__':
    confirm_db_exist()

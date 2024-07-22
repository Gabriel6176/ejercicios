import os

line='Fecha1; Fecha2; Fecha3; CUIT; D1; D2; D3; D4; D5; D6; D7; NOMBRE; OTRO'
file_name='ard.txt'
encode='latin-1'

def insert_line_top(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r', encoding=encode) as read_obj, open(dummy_file, 'w', encoding='utf-8') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

if __name__=='__main__':
    insert_line_top(file_name, line)



#file=pd.read_csv('dni2_3.txt', engine='python', encoding='latin-1')
#file.to_csv('dni2_3.txt', header=header_list, index=False)
#error ParserError: ',' expected after '"'

#solo sirve para archivos vacios
#with open('dni2_3.txt', 'w') as f:
#    wh=csv.DictWriter(f, delimiter=';', fieldnames=header_list)
#    wh.writeheader()
#
#file_new=pd.read_csv('dni2_3.txt')
#print(file_new)


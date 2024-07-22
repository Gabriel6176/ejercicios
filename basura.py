

text="24052022;01062022;30062022;30697880794;D;S;N;0,00;0,10;00;00;PAN ANTONIO'PAN PABLO'PAN GUILLERMO"
char_to_replace = {'!' : '!!',	
                   "'" : "''",
                   "#" : " "	
                   }
# Iterate over all key-value pairs in dictionary
for key, value in char_to_replace.items():
# Replace key character with value character in string
    text=text.replace(key, value)
#print(str(text))
print(f'{text}')


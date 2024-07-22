#----reemplazo de caracteres por % porcentajes

sample_string="Hoy estamos"

char_to_replace = {'!' : '%21',	
                   '#' : '%23',	
                   '$' : '%24',	
                   '&' : '%26',	
                   "'" : '%27',	
                   '(' : '%28',	
                   ')' : '%29',	
                   '*' : '%2A',	
                   '+' : '%2B',
                   ',' : '%2C',
                   '/' : '%2F',
                   ':' : '%3A',
                   ';' : '%3B',
                   '=' : '%3D',
                   '?' : '%3F',
                   '@' : '%40',
                   '[' : '%5B',
                   ']' : '%5D',
                   ' ' : '%20',
                   '"' : '%22',
                   #"%" : "%25",
                   '-' : '%2D',
                   '.' : '%2E',
                   '<' : '%3C',
                   '>' : '%3E',
                   '\\' : '%5C',
                   '^' : '%5E',
                   '_' : '%5F',
                   '`' : '%60',	
                   '{' : '%7B',
                   '|' : '%7C',
                   '}' : '%7D',
                   '~' : '%7E',
                   '´' : '%C2%B4'}


# Iterate over all key-value pairs in dictionary
for key, value in char_to_replace.items():
    # Replace key character with value character in string
    sample_string = sample_string.replace(key, value)
print(str(sample_string))

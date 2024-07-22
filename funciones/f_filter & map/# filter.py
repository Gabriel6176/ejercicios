# filter & map

#la funcion filter & map va iterando sin necesidad de hacer for
# filter(funcion, iterable) devuelve un iterador con los valores de lo iterado que cumplan la funcion

emails = ('juan@gmail.com',
        'pedro@hotmail.com',
        'mandarina',
        'bellota.com')

#opcion 3 - mas simple que todo
emailsValidos=list(filter(lambda email: '@' in email, emails))
print(emailsValidos)


#---opcion 1-----mas larga---------
def evaluar_email(email):
    #podria simplificar
    # esto ('@' in email) devuelve si o si un True o False
    #entonces seria return True o False
    if '@' in email:
        return True
    else:
        return False

#aca le puse list para que me cree una lista ya que a in iterador como filter
# no puedo hacer print(emailsValidos) si hubiese sido: emailsValidos=filter(evaluar_email, emails) 
emailsValidos=list(filter(evaluar_email, emails))
#print(emailsValidos)


#---opcion 2-----un poco mas corta--------
def evaluar_email(email):
    return '@' in email

emailsValidos=list(filter(evaluar_email, emails))

#print(emailsValidos)
#-------------------------------------


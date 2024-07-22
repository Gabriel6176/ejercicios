#validad email

numEmail=0

email=(input("Por favor ingresa tu email:"))

if(email.isdigit()):
    numEmail=numEmail + 5

if(email.isalnum()):
    numEmail=numEmail + 10

if(email.count("@")>1 or email.count(".")>1):
    numEmail=numEmail + 20

#if(email.rfind("@") and email.rfind(".")):
#    numEmail=numEmail + 1

print(numEmail)





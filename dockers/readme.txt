primero instalar docker

#despues desde cmd
docker pull python

despues debo crear un requirements.txt que diga por ejemplo
fastapi==0.59.0		#Framework web
uvicorn==0.11.5		#Servidor

#despues desde cmd
pip install -r requirements.txt
#esto lo que hace es instalar las librerias necesarias

#para ver las imagenes
docker images

#ver que docker tengo en ejecucion
docker ps

#ver los contenedores ya creados incluso los inactivos
docker ps -a

#borra contenedores inactivos
docker system prune

#para correr una imagen
docker run -it 1e4667b07108 
docker run -it - p  8000:8000 -v %cd%:usr/src simple_app

#inicia un contenedor usando una imagen
docker run -it -p 80:80 [id]

#para reiniciar el docker
#es docker attachment + el id del contenedor
docker -a 3a1d6be28940

#construye imagen
docker build -t [imagen]


#docker stop
docker stop +las dos primeras letras ya lo identifica


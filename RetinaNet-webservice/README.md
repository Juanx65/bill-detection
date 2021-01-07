## RetinaNet WebService para la Detección de billetes

### Preliminares:

Esta guía está pensada para un implementarse en un ambiente Linux. Instalar todo lo especificado en requirements.txt y ejecutar los comandos en comandos_linux.txt en el directorio principal.

Si no tiene conda, recomendamos descargar miniconda3 y añadirlo a su path, sino usar Anaconda Prompt para navegar en los ambientes virtuales.

link de descarga:
```
https://docs.conda.io/en/latest/miniconda.html
```

###### Crear un ambiente virtual con conda y activarlo

```
conda create -n <nombre_venv> python=3.6
conda activate <nombre_venv>
```

###### Instalar los requerimientos para el entorno virtual.

```
pip install -r requirements.txt
```
###### Descargar los pesos necesarios para la deteccion en el siguiente link
```
https://drive.google.com/drive/folders/11T2b6Pd0DrqtGXgqGF97kWR3wnLXEmNf?usp=sharing
```
De donde  debe descargar:

 inference_48.h5

Agregamos este archivo a la carpeta models

En la __linea 74__ de el archivo __commons.py__ se debe cambiar el valor numérico previo a la extensión ***.h5*** por el valor numérico que se muestra en el nombre del peso que se vaya a utilizar (en este caso recomendamos utilizar el peso ***inference_48.h5*** por lo que ud deberá cambiar el valor de la linea por el numero ***48***) de la siguente forma:

![Captura de el servidor web](/images_readme/pesos_retina.png)

###### Ejecutar la siguiente linea de codigo para iniciar el webservice

```
python flaskservice.py
```
Todo listo para acceder a su webservice de manera local!

si necesita saber su direccion ip, en la cmd de windows digite

```
ip addr
```
o
```
ifconfig
```
Si esta usando WSL, puede recurrir a buscarla en la cmd con
```
cat /etc/resolv.conf
```
Esto nos dará la dirección (IPv4) al servidor que nos ayudará a ejecutar la detección de billetes.


![Captura de el servidor web](/images_readme/flaskservice.png)

##### Nos conectamos desde el navegador webpreferido, ya sea en un computador o dispositivo movil y seleccionar un archivo deseado, luego hacemos click en upload para cargarlo al servidor.



# __Disfrutar de una increible detección de billetes__

![Captura de el servidor web](/images_readme/flaskServiceResult.png)

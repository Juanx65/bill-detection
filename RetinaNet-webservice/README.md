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

En la __linea 74__ de el archivo __commons.py__ se debe igualar la variable __model_path__ por el path absoluto que dirije al peso que se desea cargar al modelo, en el caso de la imagen de ejemplo  se carga el peso ***inference_37*** en el equipo de ricardo por lo que se utiliza el path de su equipo hasta el peso mencionado.

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




##### Conectarse al servidor y cargar archivo



Para acceder al webservice se deberá hacer uso de la url desde nuestro navegador preferido, desde un computador o algun dispositivo movil con la url:
```
<IPv4>:5000
```
donde <IPv4> corresponde a la dirección que se extrajo anteriormente.

![Captura de el servidor web](/images_readme/flaskservice.png)

Damos click en el __primer__  botón __choose File__  y seleccionamos un archivo de nuestra galería o bien hacemos click en el __segundo__ boton de __choose File__ para cargar una foto tomada directamente con la camara si es que el dispositivo la tiene.




# __Disfrutar de una (aun mejorable) detección de billetes__

![Captura de el servidor web](/images_readme/retinanet1.jpg)

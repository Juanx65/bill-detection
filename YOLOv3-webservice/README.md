## YOLOv3 WebService para la Detección de billetes

### Preliminares:

Esta guía está pensada para un implementarse en un ambiente Windows o Linux. Instalar todo lo especificado en requirements.txt en el directorio principal.

### Instrucciones:
Si no tiene conda instalado, recomendamos descargar miniconda3 y añadirlo a su path, en otro caso usar Anaconda Prompt para navegar en los ambientes virtuales.

Link de descarga:
```
https://docs.conda.io/en/latest/miniconda.html
```

###### Crear un ambiente virtual con conda y activarlo

```
conda create -n <nombre_venv> python=3.6
conda activate <nombre_venv>
```

###### Instalar PyTorch y torchvision

En caso de que tenga disponible GPU

```
pip install torch===1.5.0 torchvision===0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
```

En caso de que sólo se tenga disponible CPU
```
pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html##
```

###### Instalar los requerimientos para el entorno virtual.

```
pip install -r requirements.txt
```
###### Descargar los pesos necesarios para la deteccion en el siguiente link
```
https://drive.google.com/drive/folders/1oPGWvVUsr70w1GRi2xkt-H8yKOP_zgFR?usp=sharing
```
Donde:

Peso funcional CPU: yolov3_ckpt_97.pth

Peso funcional solo GPU: yolov3_ckpt_104.pth

Agregamos este archivo a la carpeta checkpoints

En las __linea 63__ y __69__  de el archivo __commons.py__ se debe cambiar el valor numérico previo a la extensión ***.pth*** por el valor numérico que se muestra en el nombre del peso que se vaya a utilizar (en este caso recomendamos utilizar el peso ***yolov3_ckpt_97.pth*** o ***yolov3_ckpt_104.pth***,  por lo que ud deberá cambiar el valor de la linea por el numero ***97*** o ***104***) de la siguente forma:


Se debe cambiar este valor en el archivo  commons.py en las lineas 63 y 69 dependiendo de el peso escogido de la siguente forma:

![Captura de el servidor web](/images_readme/pesos.png)

###### Ejecutar la siguiente linea de codigo en consola para iniciar el webservice

```
python flaskservice.py
```
Todo listo para acceder a su webservice de manera __local!__

Si necesita saber su direccion ip, en la cmd de windows utilice el siguiente comando:

```
ipconfig
```

Esto nos dará una serie de datos, de donde extraeremos  la dirección (IPv4) al servidor que nos ayudará a ejecutar la detección de billetes.



##### Conectarse al servidor y cargar archivo



Para acceder al webservice se deberá hacer uso de la url desde nuestro navegador preferido, desde un computador o algun dispositivo movil con la url:
```
<IPv4>:5000
```
donde <IPv4> corresponde a la dirección que se extrajo con el comando ipconfig.



![Captura de el servidor web](/images_readme/flaskservice.png)

Damos click en el __primer__  botón __choose File__  y seleccionamos un archivo de nuestra galería o bien hacemos click en el __segundo__ boton de __choose File__ para cargar una foto tomada directamente con la camara si es que el dispositivo la tiene.



# __Disfrutar de una (aun mejorable) detección de billetes__

![Captura de el servidor web](/images_readme/flaskServiceResult.png)
